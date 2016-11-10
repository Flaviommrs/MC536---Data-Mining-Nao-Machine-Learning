################################################################################
##
# @file non_parametric.py
# @date 2016-10-14
# @author Tiago Lobato Gimenes    (tlgimenes@gmail.com)
#
# @copyright Tiago Lobato Gimenes 2016. All rights reserved.
# 
# @section DESCRIPTION
#
################################################################################

"""
Contains a non parametric predictor and learner
"""

################################################################################

from sklearn.gaussian_process import GaussianProcessRegressor as GPR
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C

from regressor import dmining

import numpy as np

from data import data

################################################################################

class non_parametric(dmining):
    def __init__(self, kernel = None):
        self._kernel = kernel if kernel != None else C(1.0, (1e-3, 1e3)) * RBF(10, (1e-2, 1e2));
        #self._gpr = GPR(kernel=kernel, n_restarts_optimizer=9);
        self._reg = {};
        self._ssreg = {};
        self._db = None;

    def fit(self, data):
        self._db = data;

        # Do the fit proccess for each state
        for state in data._states:
            # Generates a predictor foreach symptom on this state
            self.fit_symptoms_for_state(data, state);

            # Sets Gaussian Proccess regressor for this state
            self._reg[state] = GPR(kernel=self._kernel, n_restarts_optimizer=9);

            # Gets symptoms for this state
            X = np.array([data.X()[state][symptom] for symptom in data.X()[state]]);

            # Gets disease frequency
            y = data.y()[state];

            # uses gaussian regressor for fitting
            self._reg[state].fit(X.transpose(), y);

    def fit_symptoms_for_state(self, data, state):
        for symptom in data.X()[state]:
            X = data._period.reshape(-1,1);
            y = data.X()[state][symptom];

            reg = self._ssreg[(state, symptom)] = GPR(kernel=self._kernel, n_restarts_optimizer=9);

            #print('fitstarts', X.shape, y.shape);

            reg.fit(X, y);

            #print('ok', X.shape, y.shape);

    def predict(self, period):
        y_pred = {}

        for state in data._states:
            db_pred = self.predict_symptoms_for_state(period, state);

            Xpred = np.array([db_pred.X()[state][symptom] for symptom in db_pred.X()[state]]);

            pred = self._reg[state].predict(Xpred.transpose());

            y_pred[state] = pred[0];

        return y_pred;

    def predict_symptoms_for_state(self, period, state):
        db_pred = data();

        for symptom in self._db.X()[state]:
            pred = self._ssreg[(state, symptom)].predict(period.reshape(-1,1));

            db_pred.push_sympthom(symptom, state, pred);

        return db_pred;

    def get_params(self):
        return self._gpr.get_params();

    def set_params(self, params):
        self._gpr.set_params(params);

################################################################################
