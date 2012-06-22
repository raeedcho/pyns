#!/usr/bin/env python
from setuptools import setup

classifiers =[
              'Development Status :: 4 - Beta',
              'Operating System :: OS Independent',
              'Programming Language :: Python',
              'Topic :: Scientific/Engineering',
              'Topic :: Software Development :: Libraries :: Python Modules'
              ]

setup(name="Py Neuroshare",
      version="0.3",
      description="Python port of the Neuroshare API",
      author="Ripple",
      author_email="ebarcikowski@gmail.com",
      packages=["pyns"],
#      install_requires=["numpy", "psutil", "matplotlib"],
      classifiers=classifiers,
)
        




