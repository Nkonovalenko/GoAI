import os
import sys
import multiprocessing
import six

if sys.version_info[0] == 3:
    from urllib.request import urlopen, urlretrieve
else:
    from urllib import urlopen, urlretrieve