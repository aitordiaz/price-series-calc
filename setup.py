#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read()

with open('requirements_dev.txt') as requirements_dev_file:
    requirements_dev = requirements_dev_file.read()


setup(
    author="Aitor Díaz Medina",
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Test for ETS Management ",
    install_requires=requirements.split("\n"),
    license="MIT license': 'License :: OSI Approved :: MIT License",
    long_description=readme,
    include_package_data=True,
    name='price_series_calc',
    packages=find_packages(include=['price_series_calc', 'price_series_calc.*']),
    test_suite='tests',
    tests_require=requirements_dev.split("\n"),
    url='https://github.com/aitordiaz/price-series-calc',
    version='0.0.1',
    zip_safe=False,
)