#!/usr/bin/env python
from setuptools import setup

setup(
    name='tiscovery',
    version='1.0',
    description='a network discovery tool',
    author='Count T',
    author_email='count.t.5ecurity@gmail.com',
    url='',
    packages=[],
    install_requires=[],
    entry_points={
        'console_scripts': [
            't_trace=tiscovery.traceroute:run_trace',
            't_scan=tiscovery.scan:run_scan',
            't_discover=tiscovery.discover:run_discover',
            't_sniff=tiscovery.sniffer:run_sniffer_cmd'
        ]
    }
)
