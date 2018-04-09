#!/usr/bin/env python

from __future__ import division

import os
import scipy.io as sio

def load_mat(data_dir, mat_file):
    path = os.path.join(data_dir, mat_file)
    return sio.loadmat(path)
