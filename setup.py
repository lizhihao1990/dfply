#from distutils.core import setup
from setuptools import setup

setup(
    name = 'dfply',
    version = '0.1.4',
    author = 'Kiefer Katovich',
    author_email = 'kiefer.katovich@gmail.com',
    packages = [
        'dfply',
        'dfply.vendor',
        'dfply.vendor.pandas_ply',
        'dfply.data'
    ],
    description = 'dplyr-style piping operations for pandas dataframes',
    long_description = 'See https://github.com/kieferk/dfply/blob/master/README.md for details.',
    license = 'GNU General Public License v3.0',
    url = 'https://github.com/kieferk/dfply'
)
