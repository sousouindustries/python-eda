from os.path import abspath
from os.path import dirname
from os.path import join
import os
import sys
from distutils.sysconfig import get_python_lib

from setuptools import find_packages, setup

MODULE_NAME = 'eda'
MODULE_DESC = "A Python framework for event-driven architectures."

SETUP_DIR = abspath(dirname(__file__))
README_FILE = join(SETUP_DIR, 'README.rst')
REQUIREMENTS = abspath(join(dirname(__file__), 'requirements.txt'))
EXCLUDE_FROM_PACKAGES = []
MODULE_LONG = None
if os.path.exists(README_FILE):
    MODULE_LONG = open(README_FILE).read()


# Dynamically calculate the version based,
version = __import__(MODULE_NAME).get_version()
install_requires = []


# Get the requirements from requirements.txt
if os.path.exists(REQUIREMENTS):
    with open(REQUIREMENTS) as f:
        install_requires = list(filter(bool, f.read().splitlines()))


setup(
    name=MODULE_NAME,
    version=version,
    url='https://www.sousouindustries.com/',
    author='Cochise Ruhulessin',
    author_email='cochise.ruhulessin@sousouindustries.com',
    description=MODULE_DESC,
    long_description=MODULE_LONG,
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
