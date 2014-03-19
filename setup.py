#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

setup(
    name='metricinga',
    version='1.0.0',
    description='Metricinga is a gevent-based metrics forwarder that parses performance data files from Nagios/Icinga and sends the results to Graphite',
    long_description=readme,
    author='Jeff Goldschrafe',
    author_email='jeff@holyhandgrenade.org',
    url='https://github.com/jgoldschrafe/metricinga',
    py_modules=['metricinga'],
    entry_points={
        'console_scripts': ['metricinga = metricinga:main'],
    },
    install_requires=['gevent >= 1.0rc1'],
    extras_require={'inotify': ['gevent-inotifyx']},
    license="BSD",
    zip_safe=False,
    keywords='graphite icinga metricinga nagios', 
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: System :: Monitoring',
    ],
    test_suite='tests',
)
