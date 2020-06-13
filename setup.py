#!/usr/bin/env python3
import os
import sys

from setuptools import setup


def main():
    """The main entry point."""
    with open(os.path.join(os.path.dirname(__file__), 'README.org'), 'r') as f:
        readme = f.read()
    skw = dict(
        name='conda-docker',
        description='Create minimal docker images from conda environments',
        long_description=readme,
        long_description_content_type='text/markdown',
        license='BSD-3-Clause',
        version='0.0.0',
        author='conda-forge',
        maintainer='conda-forge',
        author_email='conda-forge@googlegroups.com',
        url='https://github.com/regro/conda-docker',
        platforms='Cross Platform',
        classifiers=['Programming Language :: Python :: 3'],
        packages=['conda_docker'],
        package_dir={'conda_docker': 'conda_docker'},
        package_data={'conda_docker': ['*.xsh']},
        #scripts=scripts,
        #install_requires=['xonsh', 'lazyasd', 'ruamel.yaml', 'tqdm', 'requests', 'dataclasses'],
        python_requires=">=3.6",
        zip_safe=False,
        )
    setup(**skw)


if __name__ == '__main__':
    main()
