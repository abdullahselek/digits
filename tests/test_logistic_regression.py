#!/usr/bin/env python

import os.path
import unittest
import os

from digits import (
    logistic_regression,
    data_handler
)

class LogisticRegressionTest(unittest.TestCase):

    def test_train_model(self):
        self.assertIsNotNone(logistic_regression.train_model())

    def test_predict(self):
        training_set = logistic_regression.train_model()
        predicted_labels = logistic_regression.predict(training_set['X'][0])
        print(predicted_labels)
        self.assertIsNotNone(predicted_labels)
