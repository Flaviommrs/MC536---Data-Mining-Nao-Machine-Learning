################################################################################
##
# @file regressor.py
# @date 2016-10-14
# @author Tiago Lobato Gimenes    (tlgimenes@gmail.com)
#
# @copyright Tiago Lobato Gimenes 2016. All rights reserved.
# 
# @section DESCRIPTION
#
################################################################################

"""
Contains the interface for the machine learning algorithms
"""

################################################################################

class dmining:
    # This method should be used on the learning phase and generates the fit
    # parameters
    def fit(self, data):
        raise NotImplementedError("dmining-fit");

    # This method should predict given a time range
    def predict(self, time):
        raise NotImplementedError("dmining-predict");

    # This method should return the parameters calculated on the fit proccess
    def get_params(self):
        raise NotImplementedError("dmining-get_params");

    # This method should set the parameters calculated on the fit proccess
    # previously. One should be able to set the parameters and predict without
    # using the fit method.
    def set_params(self, params):
        raise NotImplementedError("dmining-set_params");

################################################################################
