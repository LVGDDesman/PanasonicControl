"""
Setup for the application package
"""
import sys
from setuptools import setup, find_packages

NAME = "panasonic_application"
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
    description="Panasonic application",
    author_email="",
    url="",
    keywords=[],
    packages=find_packages(),
    long_description="""\
    Contains everything needed for the panasonic application
    """
)
