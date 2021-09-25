#!/usr/bin/env python

import os.path
import sys

from setuptools import find_packages, setup

if sys.version_info < (3, 7, 0):
    sys.stderr.write("ERROR: You need Python 3.7 or later to sqlgrep.\n")
    exit(1)

# we'll import stuff from the source tree, let's ensure is on the sys path
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

# read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="sqlgrep",
    version="0.1",
    description="grep for strings in sqlite databases",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Rhet Turnbull",
    author_email="rturnbull+git@gmail.com",
    url="https://github.com/RhetTbull/sqlgrep",
    project_urls={"GitHub": "https://github.com/RhetTbull/sqlgrep"},
    download_url="https://github.com/RhetTbull/sqlgrep",
    py_modules=["sqlgrep"],
    packages=find_packages(exclude=["tests", "utils"]),
    license="License :: OSI Approved :: MIT License",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: MacOS X",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=["rich>=10.9.0", "typer>=0.4.0"],
    python_requires=">=3.7",
    entry_points={"console_scripts": ["sqlgrep=sqlgrep:main"]},
    include_package_data=True,
)
