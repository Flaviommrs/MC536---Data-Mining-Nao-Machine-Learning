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
db = db.load_csv('MG', '../trends/csvMG020161127123924305270.csv');
db = db.load_csv('MG', '../trends/csvMG120161127124312578519.csv');
db = db.load_csv('MG', '../trends/csvMG220161127135527360369.csv');
db = db.load_csv('MG', '../trends/csvMG320161127135915353338.csv');
db = db.load_csv('MG', '../trends/csvMG420161127151119853100.csv');
db = db.load_csv('MG', '../trends/csvMG520161127151507762093.csv');
db = db.load_csv('RJ', '../trends/Sudeste/csvRJ020161127192303834736.csv');
db = db.load_csv('RJ', '../trends/Sudeste/csvRJ120161127193308152490.csv');
db = db.load_csv('RJ', '../trends/Sudeste/csvRJ220161127205135510015.csv');
db = db.load_csv('RJ', '../trends/Sudeste/csvRJ320161127210139988202.csv');
db = db.load_csv('RJ', '../trends/Sudeste/csvRJ420161127222006798992.csv');
db = db.load_csv('RJ', '../trends/Sudeste/csvRJ520161127223013242722.csv');
db = db.load_csv('SP', '../trends/csvSP00.csv');
db = db.load_csv('SP', '../trends/csvSP01.csv');
db = db.load_csv('SP', '../trends/csvSP10.csv');
db = db.load_csv('SP', '../trends/csvSP11.csv');
db = db.load_csv('SP', '../trends/csvSP20.csv');
db = db.load_csv('SP', '../trends/csvSP21.csv');
db = db.load_csv('SP', '../trends/csvSP30.csv');
db = db.load_csv('SP', '../trends/csvSP31.csv');
db = db.load_csv('SP', '../trends/csvSP40.csv');
db = db.load_csv('SP', '../trends/csvSP50.csv');
db = db.load_csv('ES', '../trends/Sudeste/csvES020161127224019765276.csv');
db = db.load_csv('ES', '../trends/Sudeste/csvES120161127225442295532.csv');
db = db.load_csv('ES', '../trends/Sudeste/csvES220161127230446566809.csv');
db = db.load_csv('ES', '../trends/Sudeste/csvES320161128002313439772.csv');
db = db.load_csv('ES', '../trends/Sudeste/csvES420161128003318716096.csv');
db = db.load_csv('ES', '../trends/Sudeste/csvES420161128003318716096.csv');
db = db.load_csv('RS', '../trends/Sul/csvRS00.csv');
db = db.load_csv('PR', '../trends/Sul/csvPR00.csv');
db = db.load_csv('MT', '../trends/Centro/csvMT00.csv');
db = db.load_csv('MS', '../trends/Centro/csvMS00.csv');
db = db.load_csv('GO', '../trends/Centro/csvGO00.csv');
db = db.load_csv('SC', '../trends/Sul/csvSC00.csv');
db = db.load_csv('SC', '../trends/Sul/csvSC10.csv');

################################################################################
# How to use the DATA MINING algorithm
# creates the non parametric learnen
nonp = non_parametric(plot=False);

# Print data
db.plot('cansaco');

db_pred = nonp.predict(np.arange(0,2*db._shape[0]), db);

# Print Prediction
db_pred.plot('cansaco');

db_pred.save_csv();

plt.show();

################################################################################
