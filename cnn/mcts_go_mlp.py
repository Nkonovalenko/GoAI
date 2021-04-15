import numpy as np
from keras.models import Sequential
from keras.layers import Dense

np.random.seed(123)
# load sample data into np arrays
X = np.load('../generated_games/features-40k.npy')
Y = np.load('../generated_games/labels-40k.npy')
samples = X.shape[0]
board_size = 9*9

# Transform input into vectors of size 81 instead of 9x9
X = X.reshape(samples, board_size)
Y = Y.reshape(samples, board_size)

# Train on 90% of data, test on 10%
train_samples = int(0.8 * samples)
X_train, X_test = X[:train_samples], X[train_samples:]
Y_train, Y_test = Y[:train_samples], Y[train_samples:]

model = Sequential()
model.add(Dense(1000, activation='sigmoid', input_shape=(board_size,)))
model.add(Dense(500, activation='sigmoid'))
model.add(Dense(board_size, activation='sigmoid'))
model.summary()
 