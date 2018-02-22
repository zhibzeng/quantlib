import os
import pypandoc
from setuptools import find_packages

with open(os.path.join(os.path.dirname(__file__), 'quant/VERSION')) as f:
    version = f.read().strip()

def resolve_requirements():
    requirements = []
    with open('requirements.txt') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                requirements.append(line.strip("\n"))
    return requirements

setup_args = dict(
    name='quantlib',
    version=version,
    packages=find_packages(exclude=["*.test", "*.test.*", "test.*", "test", "script", "private", "tests"]),
    install_requires=resolve_requirements(),
    include_package_data=True,
    scripts=["scripts/quantlib"],
    url='http://quantlib.readthedocs.io/',
    license='GNU',
    author='SnowWalkerJ',
    author_email='jike3212001@163.com',
    description='A Quant library that helps data processing and backtesting',
    long_decription=pypandoc.convert("README.md", "rst"),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',

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
    setup_args['install_requires'].append('pyinstaller')

setup(**setup_args)
