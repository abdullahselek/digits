#!/usr/bin/env python

from __future__ import division

import os
import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
import math

from random import randint

def load_mat(data_dir, mat_file):
    path = os.path.join(data_dir, mat_file)
    return sio.loadmat(path)

def random_img_datas(mat_dict):
    X = mat_dict['X']
    m = np.size(X, axis=0)
    rnd_indices = [randint(0, m) for _ in range(0, 100)]
    return list(map(X.__getitem__, rnd_indices))

def display_data(data_list):
    width = int(round(math.sqrt(np.size(data_list, axis=1))))
    # Gray image
    im = plt.imshow(data_list,
                    interpolation='bilinear',
                    origin='lower',
                    extent=(-3,3,-3,3))
    # Compute rows, cols
    m, n = np.shape(data_list)
    print(m)
    height = int(n / width)
    # Compute number of items to display
    display_rows = int(math.floor(math.sqrt(m)))
    display_cols = int(math.ceil(m / display_rows))
    print(display_rows, display_cols)
    # Between images padding
    pad = 1
    # Setup blank display
    display_array = np.ones((pad + display_rows * (height + pad),
                            pad + display_cols * (width + pad)))
    print(display_array)
    # Copy each example into a patch on the display array
    curr_ex = 0
    for j in range(0, display_rows):
        for i in range(0, display_cols):
            print(curr_ex)
            if curr_ex > m - 1:
                break
            #  Copy and get the max value of the patch
            max_val = np.max(np.abs(data_list[curr_ex]))
            display_array[pad + (j - 1) * (height + pad) + np.arange(1, height),
                          pad + (i - 1) * (width + pad) + np.arange(1, width)] = np.reshape(data_list[curr_ex], (height, width)) / max_val
            curr_ex += 1
        if curr_ex > m - 1:
            break
    plt.show()
