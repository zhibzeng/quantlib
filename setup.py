from distutils.core import setup
from setuptools import find_packages

setup(
    name='quantlib',
    version='1.0.2',
    packages=find_packages(exclude=["*.test", "*.test.*", "test.*", "test", "script", "private"]),
    include_package_data=True,
    # scripts=["scripts/quantlib"],
    url='http://quantlib.readthedocs.io/',
    license='BSD',
    author='SnowWalkerJ',
    author_email='jike3212001@163.com',
    description='',
)
