import os.path
import tarfile
import gzip
import glob
import shutil

import numpy as np
from keras.utils import to_categorical

from dlgo.gosgf import Sgf_game
from dlgo.goboard_fast import Board, GameState, Move
from dlgo.gotypes import Player, Point
from dlgo.encoders.base import get_encoder_by_name

## Sampler will be used to sample training and test data from files
from dlgo.data.index_processor import KGSIndex
from dlgo.data.sampling import Sample

class GoDataProcessor:
    def __init__(self, encoder='oneplane', data_directory='data'):
        self.encoder = get_encoder_by_name(encoder, 19)
        self.data_dir = data_directory

    def load_go_data(self, data_type='train', num_samples=1000):
        index = KGSIndex(data_directory=self.data_dir)
        index.download_files()
        sampler = Sampler(data_dir=self.data_dir)
        data = sampler.draw_data(data_type, num_samples)

        zip_names = set()
        indices_by_zip_name = {}

        for filename, index in data:
            zip_names.add(filename)
            if filename not in indices_by_zip_name:
                indices_by_zip_name[filename] = []
            indices_by_zip_name[filename].append(index)
        for zip_name in zip_names:
            base_name = zip_names.replace('.tar.gz', '')
            data_file_name = base_name + data_type
            if not os.path.isfile(self.data_dir + '/' + data_file_name):
                self.process_zip(zip_name, data_file_name, indices_by_zip_name[zip_name])

        features_and_labels = self.consolidate_games(data_type, data)
        return features_and_labels
