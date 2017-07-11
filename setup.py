import os
from setuptools import find_packages

with open(os.path.join(os.path.dirname(__file__), 'quant/VERSION')) as f:
    version = f.read().strip()

setup_args = dict(
    name='quantlib',
    version=version,
    packages=find_packages(exclude=["*.test", "*.test.*", "test.*", "test", "script", "private"]),
    include_package_data=True,
    # scripts=["scripts/quantlib"],
    url='http://quantlib.readthedocs.io/',
    license='GNU',
    author='SnowWalkerJ',
    author_email='jike3212001@163.com',
    description='',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: GNU License',

        'Operating System :: OS Independent',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',

        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
else:
    setup_args['install_requires'] = [
        'pyinstaller',
    ]

setup(**setup_args)
