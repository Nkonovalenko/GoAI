from __future__ import print_function

import numpy as numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Conv2D, Flatten

np.random.seed(123)
X = np.load('../generated_games/features-200.npy')
Y = np.load('../generated_games/labels-200.npy')

samples = X.shape[0]
size = 9
input_shape = (size, size, 1)

X = X.reshape(samples, size, size, 1)

train_samples = 10000
X_train, X_test = X[:train_samples], X[train_samples:]
Y_train, Y_test = Y[:train_samples], Y[train_samples:]

model = Sequential()
model.add(Conv2D(filters=32,
                 kernel_size=(3, 3),
                 activation='sigmoid',
                 input_shape=input_shape))

