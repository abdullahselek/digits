#!/usr/bin/env python

import os.path
import unittest
import os

from digits import data_handler

class DataHandlerTest(unittest.TestCase):

    training_data = data_handler.load_mat('testdata', 'handwritten-digits.mat')

    def test_load_mat(self):
        self.assertIsNotNone(self.training_data)

    def test_random_img_datas(self):
        datas = data_handler.random_img_datas(self.training_data)
        self.assertEqual(len(list(datas)), 100)
