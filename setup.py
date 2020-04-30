#!/usr/bin/env python

# for pip >= 10
from pip._internal.req import parse_requirements
from setuptools import find_packages, setup

requirements = parse_requirements('requirements.txt')

setup(name='cabot_check_cloudwatch',
      version='0.1.2',
      description='A clouwatch check plugin for Cabot by Arachnys',
      author='Arachnys',
      author_email='techteam@arachnys.com',
      url='http://cabotapp.com',
      install_requires=requirements,
      packages=find_packages(),
    )
