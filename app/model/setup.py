"""
Setup for the viewer package
"""
import sys
from setuptools import setup, find_packages

NAME = "panasonic_model"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

setup(
    name=NAME,
    version=VERSION,
    description="Model module of the panasonic app",
    author_email="",
    url="",
    keywords=[],
    packages=find_packages(),
    long_description="""\
    Contains all the generic functions used in multiple packages of the generator.
    """
)
