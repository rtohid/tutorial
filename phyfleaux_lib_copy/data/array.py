from __future__ import annotations

__license__ = """
Copyright (c) 2020 R. Tohid

Distributed under the Boost Software License, Version 1.0. (See accompanying
file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
"""

__doc__ = """
Extends Numpy array to support data-layout transformation and global indexing.
"""

import numpy as np
from copy import deepcopy

# Tensor = deepcopy(np.ndarray)
# Tensor = np.ndarray

class Tensor:
    def __init__(self, ndarray):
        self.array = ndarray

print(Tensor.__dict__.keys())
print()
print(np.ndarray.__dict__.keys())


# def array(object, dtype=None, copy=True, order='K', subok=False, ndmin=0):
#     return np.array(object,
#                     dtype=None,
#                     copy=True,
#                     order='K',
#                     subok=False,
#                     ndmin=0)


# def ndarray(shape, arr):
#     return Tensor(shape, arr)

# shape = (2, 2)
# list_a = [1,2, 3, 4]
# arr_a = array(list_a)
# ndarray_a = ndarray(shape, arr_a)

# print(list_a)
# print(arr_a)
# print(ndarray_a)