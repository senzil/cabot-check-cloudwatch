#!/usr/bin/env python
from setuptools import find_packages, setup

with open("requirements.txt") as reqs_file:
    reqs = reqs_file.readlines()

setup(name='cabot_check_cloudwatch',
      version='0.1.2',
      description='A clouwatch check plugin for Cabot by Arachnys',
      author='Arachnys',
      author_email='techteam@arachnys.com',
      url='http://cabotapp.com',
      install_requires=reqs,
      packages=find_packages(),
    )
