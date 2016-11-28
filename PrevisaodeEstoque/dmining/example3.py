################################################################################
##
# @file example3.py
# @date 2016-11-24
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

# Load data from file
db = db.load('db.txt');

################################################################################
# How to use the DATA MINING algorithm
# creates the non parametric learnen
nonp = non_parametric(plot=False, kernel=None);

# Print data
db.plot('febre')

db_pred = nonp.predict(np.arange(0,2*db._shape[0]), db);

# Print Prediction
db_pred.plot('febre')

plt.show();

################################################################################
