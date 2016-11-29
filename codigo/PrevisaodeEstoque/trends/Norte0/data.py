################################################################################
##
# @file data.py
# @date 2016-10-14
# @author Tiago Lobato Gimenes    (tlgimenes@gmail.com)
#
# @copyright Tiago Lobato Gimenes 2016. All rights reserved.
# 
# @section DESCRIPTION
#
################################################################################

"""
Class defining how data is stored and passed to the machine learning algorithms
"""

################################################################################

import numpy as np

import pickle

from matplotlib import pyplot as plt

################################################################################

class data:
    def __init__(self):
        self._data = {};
        self._shape = None;
        self._states = set();
        self._period = None;

    # Adds new sympthon to the data
    def push_sympthom(self, symptom, state, frequency):
        assert(self._shape == None if self._shape == None else self._shape == frequency.shape);
        
        self._states = self._states.union({state});

        if state in self._data:
            self._data[state][symptom] = frequency;
        else:
            self._data[state] = {};
            self._data[state][symptom] = frequency;

        self._shape = frequency.shape;

    def push_period(self, period):
        assert(self._shape == None if self._shape == None else self._shape == period.shape);

        self._period = period;
        self._shape = period.shape;

    def y(self):
        return self._disease;

    def X(self):
        return self._data;

    def save(self, path):
        pickle.dump(self, open(path, 'wb'));

    def load(self, path):
        self = pickle.load(open(path, 'rb'));
        return self;

    def plot(self, symptom):
        size = 0;

        for state in self._data:
            size = self._data[state][symptom].size;
            plt.plot(np.arange(0, self._data[state][symptom].size),
                    self._data[state][symptom], label=symptom);

        plt.axis([0, size, 0, 100]);
        plt.show(block=False);

    def scatter(self, symptom):
        size = 0;

        for state in self._data:
            size = self._data[state][symptom].size;
            plt.scatter(np.arange(0, self._data[state][symptom].size),
                    self._data[state][symptom], c='k', label=symptom);

        plt.axis([0, size, 0, 100]);
        plt.show(block=False);

################################################################################
