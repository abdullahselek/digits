#!/usr/bin/env python

from __future__ import division

import os
import scipy.io as sio

from random import randint

def load_mat(data_dir, mat_file):
    path = os.path.join(data_dir, mat_file)
    return sio.loadmat(path)

def random_img_datas(mat_dict):
    X = mat_dict['X']
    m = len(X)
    rnd_indices = [randint(0, m) for _ in range(0, 100)]
    return list(map(X.__getitem__, rnd_indices))
