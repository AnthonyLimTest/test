from setuptools import find_packages, setup, Extension
import numpy


version = "0.13.0b6"


PACKAGE_NAME = 'mergeTest'
setup(
    name=PACKAGE_NAME,
    packages=find_packages(where='src'),
    version=version,
    package_dir={'': 'src'}
)
