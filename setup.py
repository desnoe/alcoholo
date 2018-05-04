# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='alcoholo',
    version='0.1.0',
    description='A python module to calculate alcoholometric tables as defined by OIML (International Organization of Legal Metrology)',
    long_description=readme,
    author='Olivier Desnoë',
    author_email='olivier@albatross-networks.com',
    url='https://github.com/desnoe/alcoholo',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

