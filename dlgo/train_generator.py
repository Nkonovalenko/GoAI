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
encoder = OnePlaneEncoder((go_board_rows, go_board_cols))

#Initialize Go data processor
processor = GoDataProcessor(encoder=encoder.name())

# Create 2 generators, 1 for training, 1 for testing
generator = processor.load_go_data('train', num_games, use_generator=True)
test_generator = processor.load_go_data('test', num_games, use_generator=True)

# Define neural network
input_shape = (encoder.num_planes, go_board_rows, go_board_cols)
network_layers = small.layers(input_shape)
model = Sequential
for layer in network_layers:
    model.add(layer)
model.add(Dense(num_classes, activation='softmax')) 