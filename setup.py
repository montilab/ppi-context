# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='ppi-context',
    version='1.0.0',
    description='Contextualized protein-protein interactions',
    long_description=readme,
    url='https://github.com/montilab/ppi-context',
    license=license,
    packages=find_packages(exclude=('release'))
)