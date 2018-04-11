#!/usr/bin/env python

from __future__ import division

import os
import scipy.io as sio
import numpy as np

from random import randint

def load_mat(data_dir, mat_file):
    path = os.path.join(data_dir, mat_file)
    return sio.loadmat(path)

def random_img_datas(mat_dict):
    X = mat_dict['X']
    m = np.size(X, axis=0)
    rnd_indices = [randint(0, m) for _ in range(0, 100)]
    return list(map(X.__getitem__, rnd_indices))
