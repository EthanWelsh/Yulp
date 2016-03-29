"""A setuptools based setup module.
"""

from setuptools import find_packages, setup

setup(
    name='yulp',

    version='0.0.1',

    license='MIT',

    packages=find_packages('.'),
    package_dir={'': '.'},
)
