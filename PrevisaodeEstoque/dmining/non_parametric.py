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
from sklearn.gaussian_process.kernels import RBF, WhiteKernel, RationalQuadratic, ExpSineSquared

from regressor import dmining

import numpy as np

from data import data

################################################################################

class non_parametric(dmining):
    def __init__(self, kernel = None, plot = False):
        k1 = 66.0**2 * RBF(length_scale=577.0)  # long term smooth rising trend
        k2 = 2.4**2 * RBF(length_scale=90.0) \
                * ExpSineSquared(length_scale=0.7, periodicity=50.0)  # seasonal component
        # medium term irregularity
        k3 = 0.66**2 \
                * RationalQuadratic(length_scale=1.2, alpha=0.78)
        k4 = 0.18**2 * RBF(length_scale=0.134) \
                + WhiteKernel(noise_level=0.19**2)  # noise terms
        kernel_gpml = k1 + k2 + k3 + k4
        
        self._kernel = kernel if kernel != None else kernel_gpml;
        
        self._gpr = GPR(kernel=self._kernel, alpha=0, normalize_y=True,
                n_restarts_optimizer=0 );
        self._reg = {}
        self._ssreg = {}
        self._db = None;

        self._plot = plot;

#    def predict(self, period, data):
#        y_pred = {}
#        self._db = data
#
#        for state in data._states:
#            db_pred = self.predict_symptoms_for_state(period, state);
#
#            Xpred = np.array([db_pred.X()[state][symptom] for symptom in db_pred.X()[state]]);
#            Xpred = Xpred.reshape(Xpred.shape[0], Xpred.shape[1])
#
#            # Gets symptoms for this state
#            X = np.array([data.X()[state][symptom] for symptom in data.X()[state]]);
#            # Gets disease frequency
#            y = data.y()[state];
#
#            # uses gaussian regressor for fitting
#            self._gpr.fit(X.transpose(), y);
#
#            pred = self._gpr.predict(Xpred.transpose());
#
#            y_pred[state] = pred;
#
#        return y_pred;

    def predict(self, period, db):
        y_pred = {}
        self._db = db;
        db_pred = data();

        for state in db._states:
            for symptom in self._db.X()[state]:
                X = self._db._period;
                y = self._db.X()[state][symptom];

                self._gpr.fit(X.reshape(-1,1),y.reshape(-1,1));

                pred = self._gpr.predict(period.reshape(-1,1));

                db_pred.push_sympthom(symptom, state, pred);

                if self._plot:
                    db_pred.plot(symptom);

        return db_pred;

    def predict_symptoms_for_state(self, period, state):
        db_pred = data();

        for symptom in self._db.X()[state]:
            X = self._db._period;
            y = self._db.X()[state][symptom];

            self._gpr.fit(X.reshape(-1,1),y.reshape(-1,1));

            pred = self._gpr.predict(period.reshape(-1,1));

            db_pred.push_sympthom(symptom, state, pred);

            if self._plot:
                db_pred.plot(symptom);

        return db_pred;

################################################################################
