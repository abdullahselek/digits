#!/usr/bin/env python

import os.path
import unittest
from digits import data_handler

class DataHandlerTest(unittest.TestCase):

    def test_load_mat(self):
        training_data = data_handler.load_mat('testdata', 'handwritten-digits.mat')
        self.assertIsNotNone(training_data)
