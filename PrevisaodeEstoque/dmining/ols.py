################################################################################
##
# @file ols.py
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

from regressor import dmining

import numpy as np

from data import data

################################################################################

class ols(dmining):
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
        
        X = db._period;
        y = db.X()[state][symptom];
 
        #nsample = 50
        #sig = 0.25
        #x1 = np.linspace(0, 20, nsample)
        #X = np.column_stack((x1, np.sin(x1), (x1-5)**2))
        #X = sm.add_constant(X)
        #beta = [5., 0.5, 0.5, -0.02]
        #y_true = np.dot(X, beta)
        #y = y_true + sig * np.random.normal(size=nsample)

        olsmod = sm.OLS(y, X)
        olsres = olsmod.fit()
        print(olsres.summary())

        ypred = olsres.predict(X)
        print(ypred)

        Xnew = np.column_stack((X, np.sin(X), (X-5)**2))
        print('Xnew',Xnew)
        Xnew = sm.add_constant(Xnew)
        print('Xnew',Xnew)
        ynewpred =  olsres.predict(Xnew) # predict out of sample
        print(ynewpred)

        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        ax.plot(X, y, 'o', label="Data")
        ax.plot(X, y_true, 'b-', label="True")
        ax.plot(np.hstack((X, X)), np.hstack((ypred, ynewpred)), 'r', label="OLS prediction")
        ax.legend(loc="best");

        plt.show();

        #db_pred.push_sympthom(symptom, state, arma_mod);
        
        return db_pred;

################################################################################
