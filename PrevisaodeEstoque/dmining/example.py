################################################################################
##
# @file example.py
# @date 2016-10-14
# @author Tiago Lobato Gimenes    (tlgimenes@gmail.com)
#
# @copyright Tiago Lobato Gimenes 2016. All rights reserved.
# 
# @section DESCRIPTION
#
################################################################################

"""
Contains examples on how to use these classes
"""

################################################################################

import numpy as np

from non_parametric import non_parametric
from data import data

from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels \
    import RBF, WhiteKernel, RationalQuadratic, ExpSineSquared

from matplotlib import pyplot as plt

from mock import mock

################################################################################
# Create data
db = data();

################################################################################
## Push frequencies for each state for each sympthom
db.push_sympthom('dor_de_cabeca', 'SP', mock['dor_de_cabeca']);

db.push_sympthom('febre', 'SP', mock['febre']);

# Push the period
db.push_period(np.arange(0, mock['dengue'].size));

################################################################################
# How to retrieve the frequency
frequency_MG = db._data['SP']['dor_de_cabeca'];

################################################################################
# How to use the DATA MINING algorithm
# creates the non parametric learner
nonp = non_parametric(plot=False);

db.plot('dor_de_cabeca')
db.plot('febre')

db_pred = nonp.predict(np.arange(0,450), db);

print('LogLikelihood', nonp._gpr.log_marginal_likelihood(nonp._gpr.kernel_.theta))

db_pred.plot('dor_de_cabeca')
db_pred.plot('febre')
plt.show();

################################################################################
