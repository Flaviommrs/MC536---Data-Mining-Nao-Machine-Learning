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
import csv

from pandas import date_range
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

    def load_csv(self, state, path):
        csvfile = open(path, 'r');
        spamreader = csv.reader(csvfile, delimiter=',');
        symptoms = np.array([]);
        frequencies = {};
        for row in spamreader:
            if spamreader.line_num == 1:
                symptoms = np.array(row);
                for i in range(symptoms.size):
                    frequencies[str(symptoms[i])] = [];
            else:
                for i in range(symptoms.size):
                    frequencies[str(symptoms[i])].append(row[i])

        for f in frequencies:
            if f != 'Date':
                self.push_sympthom(f, state, np.array(frequencies[f]));

        size = np.array(frequencies['Date']).size
        self.push_period(np.linspace(0,size,size));

        return self;

    def save_csv(self):
        symptoms = [];

        for state in self._data:
            for s in self._data[state]:
                symptoms.append(s);

        for s in symptoms:
            csvfile = open('./predictions/'+s+'.csv', 'w')
            spanwriter = csv.writer(csvfile, delimiter=',',quoting=csv.QUOTE_MINIMAL);
            spanwriter.writerow([s.upper()]);
            for state in self._data:
                if s in self._data[state]:
                    data = [state];
                    [data.append(d[0]) for d in self._data[state][s]]
                    spanwriter.writerow(data);
            date = date_range(start='1/4/2004', periods=len(data)-1, freq='7D')
            date = date.insert(0, 'Date');
            spanwriter.writerow(date)

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
