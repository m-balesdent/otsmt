#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from setuptools import setup, find_packages
import sys

# Get the version from __init__.py
with open('otsmt/__init__.py') as fid:
    for line in fid:
        if line.startswith('__version__'):
            version = line.strip().split()[-1][1:-1]
            break

if sys.version_info < (3, 0):
    install_requires.append('logging')

setup(
    # library name
    name='otsmt',

    # code version
    version=version,

    # list libraries to be imported
    packages=find_packages(),


    # Descriptions
    description="Class implementing bindings from smt to OpenTURNS",
    long_description=open('README.rst').read(),
	
    setup_requires=['pytest-runner',
	'cython'],
    
    install_requires=['numpy',
			'smt',
		     'openturns',
			 'matplotlib'],
    tests_require=['pytest'],

)
