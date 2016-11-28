################################################################################
##
# @file run_mock.py
# @date 2016-11-28
# @author Tiago Lobato Gimenes    (tlgimenes@gmail.com)
#
# @copyright Tiago Lobato Gimenes 2016. All rights reserved.
# 
# @section DESCRIPTION
#
################################################################################

"""

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

db = db.load_csv('BR', './mock.csv');

################################################################################
# How to use the DATA MINING algorithm
# creates the non parametric learner
nonp = non_parametric(plot=False);

#db.plot('esquistossomose')
db.plot('febre')
#db.plot('diarreia')

db_pred = nonp.predict(np.arange(0,350), db);

#db_pred.plot('esquistossomose')
db_pred.plot('febre')
#db_pred.plot('diarreia')
plt.show();

################################################################################
################################################################################
