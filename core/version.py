from __future__ import absolute_import, division, print_function
from os.path import join as pjoin

# Format expected by setup.py and doc/source/conf.py: string of form "X.Y.Z"
_version_major = 0
_version_minor = 0
_version_micro = 0  # use '' for first of series, number for 1 and above
_version_extra = 'dev0'
# _version_extra = ''  # Uncomment this for full releases

# Construct full version string from these.
_ver = [_version_major, _version_minor]
if _version_micro:
    _ver.append(_version_micro)
if _version_extra:
    _ver.append(_version_extra)

__version__ = '.'.join(map(str, _ver))

CLASSIFIERS = ["Development Status :: 3 - Alpha",
               "Environment :: Console",
               "Intended Audience :: Science/Research",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent",
               "Programming Language :: Python :: 3.6",
               "Topic :: Scientific/Engineering"]

# Description should be a one-liner:
description = "capstone project for the DIRECT course"
# Long description will go up on the pypi page
long_description = """

DIRECT Capstone
===============
Capstone project for the DIRECT course

"""

NAME = "directcap"
MAINTAINER = "Wesley Beckner"
MAINTAINER_EMAIL = "wab665@uw.edu"
DESCRIPTION = description
LONG_DESCRIPTION = long_description
URL = "http://github.com/DIRECT_capstone"
DOWNLOAD_URL = ""
LICENSE = "MIT"
AUTHOR = "Wesley Beckner"
AUTHOR_EMAIL = "wab665@uw.edu"
PLATFORMS = "OS Independent"
MAJOR = _version_major
MINOR = _version_minor
MICRO = _version_micro
VERSION = __version__
PACKAGE_DATA = {'core': [pjoin('data', '*')]}
REQUIRES = ["numpy"]
