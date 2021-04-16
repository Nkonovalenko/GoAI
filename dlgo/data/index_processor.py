import os
import sys
import multiprocessing
import six

if sys.version_info[0] == 3:
    from urllib.request import urlopen, urlretrieve
else:
    from urllib import urlopen, urlretrieve


class KGSIndex:

    def __init__(self,
                 kgs_url='http://u-go.net/gamerecords/',
                 index_page='kgs_index.html',
                 data_directory='data'):
        """Create an index of zip files containing SGF data of actual Go Games on KGS.
        Parameters:
        -----------
        kgs_url: URL with links to zip files of games
        index_page: Name of local html file of kgs_url
        data_directory: name of directory relative to current path to store SGF data
        """
        self.kgs_url = kgs_url
        self.index_page = index_page
        self.data_directory = data_directory
        self.file_info = []
        self.urls = []
        self.load_index()  # Load index on creation

