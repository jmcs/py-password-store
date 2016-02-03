#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

version = '0.2'

# TODO add README and long_description

setup(
    name='password-store',
    packages=find_packages(),
    version=version,
    description='Password Store Wrapper',
    author='João Santos',
    author_email='jmcs@jsantos.eu',
    url='https://github.com/jmcs/py-password-store',
    license='MIT License',
    install_requires=['pyyaml'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
    ],
)
