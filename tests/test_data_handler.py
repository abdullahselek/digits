#!/usr/bin/env python

import os.path
import unittest
import os
import matplotlib.pyplot as plt

from digits import data_handler
from threading import Timer

def close_figure():
        plt.close()

class DataHandlerTest(unittest.TestCase):

    training_data = data_handler.load_mat('testdata', 'handwritten-digits.mat')

    def test_load_mat(self):
        self.assertIsNotNone(self.training_data)

    def test_random_img_datas(self):
        datas = data_handler.random_img_datas(self.training_data)
        self.assertEqual(len(datas), 100)

    def test_display_data(self):
        datas = data_handler.random_img_datas(self.training_data)
        fig = data_handler.display_data(datas)
        self.assertIsNotNone(fig)
        t = Timer(10.0, close_figure)
        t.start()
