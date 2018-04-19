#!/usr/bin/env python

from __future__ import division

import numpy as np

from digits import data_handler
from sklearn.linear_model import LogisticRegression

# all parameters not specified are set to their defaults
logistic_regr = LogisticRegression()

def train_model():
    training_data = data_handler.load_mat('digits/training-set', 'handwritten-digits.mat')
    logistic_regr.fit(training_data['X'], np.ravel(training_data['y']))
    return training_data

def predict(X):
    return logistic_regr.predict(np.reshape(X, (1, -1)))
