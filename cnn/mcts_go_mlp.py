import numpy as np
from keras.models import Sequential
from keras.layers import Dense

np.random.seed(123)
# load sample data into np arrays
X = np.load('../generated_games/features-40k.npy')
Y = np.load('../generated_games/labels-40k.npy')
