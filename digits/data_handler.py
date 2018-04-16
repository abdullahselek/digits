#!/usr/bin/env python

from __future__ import division

import os
import scipy.io as sio
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import math

from random import randint
from mpl_toolkits.axes_grid1 import ImageGrid

def load_mat(data_dir, mat_file):
    path = os.path.join(data_dir, mat_file)
    return sio.loadmat(path)

def random_img_datas(mat_dict):
    X = mat_dict['X']
    m = np.size(X, axis=0)
    rnd_indices = [randint(0, m-1) for _ in range(0, 100)]
    return list(map(X.__getitem__, rnd_indices))

def display_data(data_list):
    """Display 2D data in a nice grid.
    Args:
      data_list (array): Data contains image traning sets.
    Returns:
      fig (figure): matplotlib figure.
    """
    fig = plt.figure(num=None, figsize=(20, 20), dpi=80)
    grid = ImageGrid(fig,
                     141,
                     nrows_ncols=(10, 10))

    for i in range(100):
        img_data = np.reshape(data_list[i], (20, 20))
        _ = grid[i].imshow(img_data, interpolation="nearest")

    plt.show()
    return fig
