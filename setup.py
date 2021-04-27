from setuptools import setup
from setuptools import find_packages

setup(name='dlgo',
      version='0.1',
      description='GoAI',
      url='https://github.com/Nkonovalenko/GoAI',
      install_requires=['tensorflow', 'keras', 'gomill', 'Flask>=0.10.1', 'Flask-Cors', 'future', 'h5py', 'six'],
      license='MIT',
      packages=find_packages(),
      zip_safe=False)