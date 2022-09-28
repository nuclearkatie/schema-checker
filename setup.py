#!/usr/bin/env python
from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(name="cyclussc",
      version='0.1',
      description='Tool to check if all prototypes in a cyclus simulation have been deployed by NullInst',
      long_description_content_type="text/markdown",
      author='Katie Mummah',
      author_email='katiemummah@gmail.com',
      packages=find_packages(),
      entry_points={
          'console_scripts' : ['cyclussc = src.schema_checker:main']
      })