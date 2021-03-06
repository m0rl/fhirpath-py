#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
from io import open

from setuptools import setup, find_packages


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, "__init__.py")).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version("fhirpathpy")

with open("README.md") as f:
    long_description = f.read()


setup(
    name="fhirpathpy",
    version=version,
    description="FHIRPath implementation in Python",
    license="",
    project_urls={"Source Code": "https://github.com/beda-software/fhirpath-py",},
    packages=["fhirpathpy"],
    include_package_data=True,
    zip_safe=False,
    install_requires=["antlr4-python3-runtime==4.8"],
)
