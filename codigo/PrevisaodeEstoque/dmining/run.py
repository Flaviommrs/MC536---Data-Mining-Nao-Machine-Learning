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
db = db.load_csv('MG', '../trends/Sudeste/csvMG020161127123924305270.csv');
db = db.load_csv('MG', '../trends/Sudeste/csvMG120161127124312578519.csv');
db = db.load_csv('MG', '../trends/Sudeste/csvMG220161127135527360369.csv');
db = db.load_csv('MG', '../trends/Sudeste/csvMG320161127135915353338.csv');
db = db.load_csv('MG', '../trends/Sudeste/csvMG420161127151119853100.csv');
db = db.load_csv('MG', '../trends/Sudeste/csvMG520161127151507762093.csv');
db = db.load_csv('RJ', '../trends/Sudeste/csvRJ020161127192303834736.csv');
db = db.load_csv('RJ', '../trends/Sudeste/csvRJ120161127193308152490.csv');
db = db.load_csv('RJ', '../trends/Sudeste/csvRJ220161127205135510015.csv');
db = db.load_csv('RJ', '../trends/Sudeste/csvRJ320161127210139988202.csv');
db = db.load_csv('RJ', '../trends/Sudeste/csvRJ420161127222006798992.csv');
db = db.load_csv('RJ', '../trends/Sudeste/csvRJ520161127223013242722.csv');
db = db.load_csv('SP', '../trends/Sudeste/csvSP00.csv');
db = db.load_csv('SP', '../trends/Sudeste/csvSP01.csv');
db = db.load_csv('SP', '../trends/Sudeste/csvSP10.csv');
db = db.load_csv('SP', '../trends/Sudeste/csvSP11.csv');
db = db.load_csv('SP', '../trends/Sudeste/csvSP20.csv');
db = db.load_csv('SP', '../trends/Sudeste/csvSP21.csv');
db = db.load_csv('SP', '../trends/Sudeste/csvSP30.csv');
db = db.load_csv('SP', '../trends/Sudeste/csvSP31.csv');
db = db.load_csv('SP', '../trends/Sudeste/csvSP40.csv');
db = db.load_csv('SP', '../trends/Sudeste/csvSP50.csv');
db = db.load_csv('ES', '../trends/Sudeste/csvES020161127224019765276.csv');
db = db.load_csv('ES', '../trends/Sudeste/csvES120161127225442295532.csv');
db = db.load_csv('ES', '../trends/Sudeste/csvES220161127230446566809.csv');
db = db.load_csv('ES', '../trends/Sudeste/csvES320161128002313439772.csv');
db = db.load_csv('ES', '../trends/Sudeste/csvES420161128003318716096.csv');
db = db.load_csv('ES', '../trends/Sudeste/csvES420161128003318716096.csv');
db = db.load_csv('MT', '../trends/Centro/csvMT00.csv');
db = db.load_csv('MT', '../trends/Centro/csvMT01.csv');
db = db.load_csv('MT', '../trends/Centro/csvMT02.csv');
db = db.load_csv('MS', '../trends/Centro/csvMS00.csv');
db = db.load_csv('MS', '../trends/Centro/csvMS01.csv');
db = db.load_csv('MS', '../trends/Centro/csvMS02.csv');
db = db.load_csv('GO', '../trends/Centro/csvGO00.csv');
db = db.load_csv('GO', '../trends/Centro/csvGO01.csv');
db = db.load_csv('GO', '../trends/Centro/csvGO02.csv');
db = db.load_csv('DF', '../trends/Centro/csvDF00.csv');
db = db.load_csv('DF', '../trends/Centro/csvDF01.csv');
db = db.load_csv('DF', '../trends/Centro/csvDF02.csv');
db = db.load_csv('SC', '../trends/Sul/csvSC00.csv');
db = db.load_csv('SC', '../trends/Sul/csvSC10.csv');
db = db.load_csv('RS', '../trends/Sul/csvRS00.csv');
db = db.load_csv('RS', '../trends/Sul/csvRS01.csv');
db = db.load_csv('RS', '../trends/Sul/csvRS02.csv');
db = db.load_csv('PR', '../trends/Sul/csvPR00.csv');
db = db.load_csv('PR', '../trends/Sul/csvPR01.csv');
db = db.load_csv('PR', '../trends/Sul/csvPR02.csv');
db = db.load_csv('AC', '../trends/Norte0/csvAC00.csv');
db = db.load_csv('AC', '../trends/Norte0/csvAC01.csv');
db = db.load_csv('AC', '../trends/Norte0/csvAC03.csv');
db = db.load_csv('AM', '../trends/Norte0/csvAM00.csv');
db = db.load_csv('AM', '../trends/Norte0/csvAM01.csv');
db = db.load_csv('AM', '../trends/Norte0/csvAM03.csv');
db = db.load_csv('AP', '../trends/Norte0/csvAP00.csv');
db = db.load_csv('AP', '../trends/Norte0/csvAP01.csv');
db = db.load_csv('AP', '../trends/Norte0/csvAP02.csv');
db = db.load_csv('PA', '../trends/Norte0/csvPA00.csv');
db = db.load_csv('PA', '../trends/Norte0/csvPA01.csv');
db = db.load_csv('PA', '../trends/Norte0/csvPA02.csv');
db = db.load_csv('RO', '../trends/Norte0/csvRO00.csv');
db = db.load_csv('RO', '../trends/Norte0/csvRO01.csv');
db = db.load_csv('RO', '../trends/Norte0/csvRO02.csv');
db = db.load_csv('RR', '../trends/Norte0/csvRR00.csv');
db = db.load_csv('RR', '../trends/Norte0/csvRR01.csv');
db = db.load_csv('RR', '../trends/Norte0/csvRR02.csv');
db = db.load_csv('TO', '../trends/Norte0/csvTO00.csv');
db = db.load_csv('TO', '../trends/Norte0/csvTO01.csv');
db = db.load_csv('TO', '../trends/Norte0/csvTO02.csv');
db = db.load_csv('AL', '../trends/Nordeste0/csvAL00.csv');
db = db.load_csv('AL', '../trends/Nordeste0/csvAL01.csv');
db = db.load_csv('AL', '../trends/Nordeste0/csvAL02.csv');
db = db.load_csv('BA', '../trends/Nordeste0/csvBA00.csv');
db = db.load_csv('BA', '../trends/Nordeste0/csvBA01.csv');
db = db.load_csv('BA', '../trends/Nordeste0/csvBA02.csv');
db = db.load_csv('CE', '../trends/Nordeste0/csvCE00.csv');
db = db.load_csv('CE', '../trends/Nordeste0/csvCE01.csv');
db = db.load_csv('CE', '../trends/Nordeste0/csvCE02.csv');
db = db.load_csv('MA', '../trends/Nordeste0/csvMA00.csv');
db = db.load_csv('MA', '../trends/Nordeste0/csvMA01.csv');
db = db.load_csv('MA', '../trends/Nordeste0/csvMA02.csv');
db = db.load_csv('PB', '../trends/Nordeste0/csvPB00.csv');
db = db.load_csv('PB', '../trends/Nordeste0/csvPB01.csv');
db = db.load_csv('PB', '../trends/Nordeste0/csvPB02.csv');
db = db.load_csv('PE', '../trends/Nordeste0/csvPE00.csv');
db = db.load_csv('PE', '../trends/Nordeste0/csvPE01.csv');
db = db.load_csv('PE', '../trends/Nordeste0/csvPE02.csv');
db = db.load_csv('PI', '../trends/Nordeste0/csvPI00.csv');
db = db.load_csv('PI', '../trends/Nordeste0/csvPI01.csv');
db = db.load_csv('PI', '../trends/Nordeste0/csvPI02.csv');
db = db.load_csv('RN', '../trends/Nordeste0/csvRN00.csv');
db = db.load_csv('RN', '../trends/Nordeste0/csvRN01.csv');
db = db.load_csv('RN', '../trends/Nordeste0/csvRN02.csv');
db = db.load_csv('SE', '../trends/Nordeste0/csvSE00.csv');
db = db.load_csv('SE', '../trends/Nordeste0/csvSE01.csv');
db = db.load_csv('SE', '../trends/Nordeste0/csvSE02.csv');

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
