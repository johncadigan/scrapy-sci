#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='scrapy-sci',
    version='0.1.0',
    description='Improve your scrapy pipeline with machine learning',
    long_description=readme + '\n\n' + history,
    author='John Cadigan',
    author_email='johnpaulcadigan@gmail.com',
    url='https://github.com/johncadigan/scrapy-sci',
    packages=[
        'scrapy_sci',
        "scrapy_sci.commands",
        "scrapy_sci.templates",
    ],
    package_dir={'scrapy_sci':
                 'scrapy_sci'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='machine learning',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Framework :: Scrapy',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
