#!/usr/bin/env python

import os.path
import unittest
import os

from digits import logistic_regression

class LogisticRegressionTest(unittest.TestCase):

    def test_train_model(self):
        self.assertTrue(logistic_regression.train_model())
