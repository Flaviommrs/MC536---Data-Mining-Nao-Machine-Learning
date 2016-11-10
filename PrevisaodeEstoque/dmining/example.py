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

from matplotlib import pyplot as plt

from mock import mock

################################################################################
# Create data
db = data();

################################################################################
## Push frequencies for each state for each sympthom
db.push_sympthom('dor_de_cabeca', 'SP', mock['dor_de_cabeca']);

db.push_sympthom('febre', 'SP', mock['febre']);

# Push disease frequency
db.push_disease('SP', mock['dengue']);

# Push the period
db.push_period(np.arange(0, mock['dengue'].size));

################################################################################
# How to retrieve the frequency
frequency_MG = db._data['SP']['dor_de_cabeca'];

################################################################################

#db.plot('dor_de_cabeca');
db.plot('febre');
#db.plot();

################################################################################
# How to use the DATA MINING algorithm
# creates the non parametric learner
nonp = non_parametric();

nonp.fit(db);

#nonp.predict(np.arange(0,20), db);

db_pred = nonp.predict_symptoms_for_state(np.arange(0, 300), 'SP');

db_pred.plot('febre');

a = input();

################################################################################
