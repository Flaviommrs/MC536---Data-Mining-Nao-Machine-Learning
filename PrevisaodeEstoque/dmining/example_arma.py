################################################################################
##
# @file example_arma.py
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

################################################################################

import numpy as np

from timeseries import timeseries
from data import data

from matplotlib import pyplot as plt

################################################################################
# Create data
db = data();

# Load data from file
db = db.load('db.txt');

################################################################################
# How to use the DATA MINING algorithm
# creates the non parametric learner
ts = timeseries();

db_pred = ts.predict_for('SP', 'febre', np.arange(0,2*db._shape[0]), db);

#db.plot('febre')
#db_pred.plot('febre')
#
#plt.show();

################################################################################
