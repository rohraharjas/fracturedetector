from setuptools import find_packages, setup
from typing import List

SHORT_DESCRIPTION = "FractureDetector Package is a CNN model that checks if a X-Ray image shows a fracture."

with open("README.md", "r") as fh: 
    LONG_DESCRIPTION = fh.read()

setup(
 name = 'FractureDetector',
version='0.0.10',
author='Harjas Rohra',
author_email='<hrohra2004@gmaill.com>',
description = SHORT_DESCRIPTION,
long_description = LONG_DESCRIPTION,
long_description_content_type = "text/markdown",
license="MIT",
license_files= ("LICENSE.txt",),
packages=find_packages(),
install_requires = ['pillow', 'joblib', 'numpy'],
classifiers=[ 
        "Programming Language :: Python :: 3", 
        "Operating System :: OS Independent", 
    ], 
)