################################################################################
##
# @file run.py
# @date 2016-11-27
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

from pandas import date_range

################################################################################
# Create data
db = data();

# Load data from file
db = db.load_csv('MG', '../trends/csvMG02016-11-27 12:39:24.305270.csv');
db = db.load_csv('MG', '../trends/csvMG12016-11-27 12:43:12.578519.csv');
db = db.load_csv('MG', '../trends/csvMG22016-11-27 13:55:27.360369.csv');
db = db.load_csv('MG', '../trends/csvMG32016-11-27 13:59:15.353338.csv');
db = db.load_csv('MG', '../trends/csvMG42016-11-27 15:11:19.853100.csv');
db = db.load_csv('MG', '../trends/csvMG52016-11-27 15:15:07.762093.csv');

################################################################################
# How to use the DATA MINING algorithm
# creates the non parametric learnen
nonp = non_parametric(plot=False);

# Print data
db.plot('febre');

db_pred = nonp.predict(np.arange(0,2*db._shape[0]), db);

# Print Prediction
db_pred.plot('febre');

db_pred.save_csv();

plt.show();

################################################################################
