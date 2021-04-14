from __future__ import print_function

import numpy as numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Conv2D, Flatten

np.random.seed(123)
X = np.load('../generated_games/features-200.npy')
Y = np.load('../generated_games/labels-200.npy')

