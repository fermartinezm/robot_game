import os
import sys

from setuptools import setup, find_packages

with open('requirements.txt') as f:

    requirements_file_content = f.read().splitlines()

requirements = []
links = []
for r in requirements_file_content:
    if 'git+' in r[:4]:
        os.system("pip install " + r)
    else:
        requirements.append(r)


setup(name='robot',
      version='1.0',
      description='REA exercise',
      author='',
      author_email='',
      install_requires=requirements,
      dependency_links=links,
      packages=find_packages(),
      data_files=[],
      license='Apache License 2.0',
      classifiers=[
          "Environment :: Console",
          "Intended Audience :: Developers",
          "Natural Language :: English",
          "Operating System :: POSIX :: Linux",
          "Programming Language :: Python :: 3.6",
          "Topic :: System"
      ],
      entry_points=''
    ,)
