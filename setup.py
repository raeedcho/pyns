#!/usr/bin/env python
from setuptools import find_packages, setup

classifiers = [
    'Development Status :: 4 - Beta',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Scientific/Engineering',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'License :: OSI Approved :: GNU General Public License (GPL)'
]

setup(name="pyns",
      version="0.4.2",
      description="Python port of the Neuroshare API",
      author="Ripple LLC",
      author_email="support@rppl.com",
      classifiers=classifiers,
      install_requires=['matplotlib', 'numpy', 'psutil'],
      packages = find_packages(),
      )
