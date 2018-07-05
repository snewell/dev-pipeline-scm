#!/usr/bin/python3

from setuptools import setup, find_packages

setup(
    name="dev-pipeline-scm",
    version="0.2.0",
    package_dir={
        "": "lib"
    },
    packages=find_packages("lib"),

    install_requires=[
        'dev-pipeline-core >= 0.2.0'
    ],

    entry_points={
        'devpipeline.drivers': [
            'checkout = devpipeline_scm.checkout:main'
        ],

        'devpipeline.scms': [
            'nothing = devpipeline_scm.scm:_nothing_scm',
        ]
    },

    author="Stephen Newell",
    description="scm tooling for dev-pipeline",
    license="BSD-2"
)
