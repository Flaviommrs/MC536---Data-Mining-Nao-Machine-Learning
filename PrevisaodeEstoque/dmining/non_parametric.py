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
from sklearn.kernel_ridge import KernelRidge

from regressor import dmining

import numpy as np

from data import data

################################################################################

class non_parametric(dmining):
    def __init__(self, kernel = None, plot = False):
        kernels = []
        kernels.append(RBF(length_scale=600.0))                                                        # long term smooth rising trend
        kernels.append(2*RBF(length_scale=300.0) * ExpSineSquared(length_scale=0.1, periodicity=60.0)) # seasonal component
        #kernels.append(ExpSineSquared(length_scale=0.1, periodicity=40.0))                             # seasonal component
        #kernels.append(RationalQuadratic(length_scale=0.01, alpha=20)) 
        #kernels.append(WhiteKernel(noise_level=100)) 
        
        kernel = kernels[0]
        for k in kernels[1:]:
            kernel = k + kernel

        kernel_gpml = kernel
        
        self._kernel = kernel if kernel != None else kernel_gpml;
        
        self._gpr = KernelRidge(kernel = self._kernel);
        #self._gpr = GPR(kernel = self._kernel, normalize_y=True, n_restarts_optimizer=1);
        self._reg = {}
        self._ssreg = {}
        self._db = None;

        self._plot = plot;

    def predict_for(self, state, symptom, period, db):
        self._db = db;
        db_pred = data();

        X = self._db._period;
        y = self._db.X()[state][symptom];
        
        self._gpr.fit(X.reshape(-1,1),y.reshape(-1,1));
        
        pred = self._gpr.predict(period.reshape(-1,1));
        
        db_pred.push_sympthom(symptom, state, pred);
        
        return db_pred;

    def predict(self, period, db):
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
