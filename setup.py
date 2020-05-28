# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = ""

setup(
    long_description=readme,
    name="simple-back",
    version="0.4a2",
    python_requires="==3.*,>=3.7.0",
    author="Christoph Minixhofer",
    author_email="christoph.minixhofer@gmail.com",
    packages=["simple_back"],
    package_dir={"": "."},
    package_data={},
    install_requires=[
        "numpy==1.*,>=1.18.4",
        "pandas==1.*,>=1.0.3",
        "pandas-market-calendars==1.*,>=1.3.5",
        "requests-html==0.*,>=0.10.0",
        "yahoo-fin==0.*,>=0.8.5",
    ],
    extras_require={"dev": ["pytest==5.*,>=5.2.0"]},
)
