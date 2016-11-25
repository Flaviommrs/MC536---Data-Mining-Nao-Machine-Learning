################################################################################
##
# @file timeseries.py
# @date 2016-11-25
# @author Tiago Lobato Gimenes    (tlgimenes@gmail.com)
#
# @copyright Tiago Lobato Gimenes 2016. All rights reserved.
# 
# @section DESCRIPTION
#
################################################################################

"""

"""
import statsmodels.api as sm
from statsmodels.tsa.arima_process import arma_generate_sample

from regressor import dmining

import numpy as np

import pandas as pd

from data import data

################################################################################

class timeseries(dmining):
    def predict(self, period, db):
        db_pred = data();

        for state in db._states:
            for symptom in self._db.X()[state]:
                X = db._period;
                y = db.X()[state][symptom];

                arma_mod = sm.tsa.ARMA(y, (2,0)).fit()

                db_pred.push_sympthom(symptom, state,
                        arma_mod.predict(arma_mod.params, 0, 500));

        return db_pred;

    def predict_for(self, state, symptom, period, db):
        db_pred = data();
        
        y = db.X()[state][symptom][230:];
        
        #arparams = np.array([.75, -.25])
        #maparams = np.array([.65, .35])
        #arparams = np.r_[1, -arparams]
        #maparam = np.r_[1, maparams]
        #nobs = 250
        #y = arma_generate_sample(arparams, maparams, nobs)    

        dates = sm.tsa.datetools.dates_from_range('1980m1', length=y.size)
        y = pd.TimeSeries(y, index=dates)
        arma_mod = sm.tsa.ARMA(y, order=(20,0))
        arma_res = arma_mod.fit(trend='c', disp=-1)
        
        print(arma_res.params)

        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(10,8))
        fig = arma_res.plot_predict(start=0, end=2*y.size, ax=ax)
        legend = ax.legend(loc='upper left')

        plt.show();

        #db_pred.push_sympthom(symptom, state, arma_mod);
        
        return db_pred;

################################################################################
