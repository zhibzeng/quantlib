from distutils.core import setup
from setuptools import find_packages

setup(
    name='quantlib',
    version='1.0.1',
    packages=find_packages(exclude=["*.test", "*.test.*", "test.*", "test", "script"]),
    # scripts=["scripts/quantlib"],
    url='',
    license='BSD',
    author='SnowWalkerJ',
    author_email='jike3212001@163.com',
    description='',
)
