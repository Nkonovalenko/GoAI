"""Network with 3 Fully Connected layers, ReLu activation."""
from keras.layers.core import Dense, Activation, Flatten

def layers(input_shape):
    return [
        Dense(128, input_shape=input_shape),
        Activation('relu'),
        Dense(128, input_shape=input_shape),
        Activation('relu'),
        Flatten(),
        Dense(128),
        Activation('relu'),
    ]