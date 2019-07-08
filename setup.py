#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
File: /setup.py
Project: aapt
Description:
Created By: Tao.Hu 2019-07-08
-----
Last Modified: 2019-07-08 02:03:42 pm
Modified By: Tao.Hu
-----
'''
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="aapt",
    version="1.0.1",
    keywords=("aapt", "apktool"),
    description="Android Asset Packaging Tool for Python3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HuMoran/aapt",
    author="Tao.Hu",
    author_email="htax2013@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
