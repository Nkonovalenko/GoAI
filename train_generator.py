"""File to train generator."""
from dlgo.data.parallel_processor import GoDataProcessor
from dlgo.encoders.oneplane import OnePlaneEncoder

from dlgo.networks import small
from keras.models import Sequential
from keras.layers.core import Dense
from keras.callbacks import ModelCheckpoint

go_board_rows, go_board_cols = 19, 19
num_classes = go_board_rows * go_board_cols
num_games = 100

# Create encoder of 19x19 size 
print("Creating Encoder...")
encoder = OnePlaneEncoder((go_board_rows, go_board_cols))

#Initialize Go data processor
print("Creating processor...")
processor = GoDataProcessor(encoder=encoder.name())

# Create 2 generators, 1 for training, 1 for testing
print("Creating train generator...")
generator = processor.load_go_data('train', num_samples=num_games,use_generator=True)
print("Creating test generator...")
test_generator = processor.load_go_data('test', num_games, use_generator=True)

# Define neural network based on small model
print("Defining neural network...")
input_shape = (encoder.num_planes, go_board_rows, go_board_cols)
network_layers = small.layers(input_shape)
model = Sequential()
for layer in network_layers:
    model.add(layer)
# After adding all small layers, add fully connected layer with softmax activation
model.add(Dense(num_classes, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

# Fit keras model with generators
epochs = 1000
batch_size = 128
print("Training neural network...")
samp = generator.get_num_samples()
print("Num samples: ", samp)
print("Batch size: ", batch_size)
print("Steps: ", samp/batch_size)
model.fit(x=generator.generate(batch_size, num_classes), epochs=epochs,
                    steps_per_epoch=generator.get_num_samples()/batch_size,
                    validation_steps=test_generator.get_num_samples()/batch_size,
                   callbacks=[ModelCheckpoint('checkpoints/small_model_epoch_{epoch}.h5')])
print("Evaluating neural network...")
model.evaluate(
    x=test_generator.generate(batch_size, num_classes),
    steps=test_generator.get_num_samples() / batch_size) 