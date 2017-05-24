#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('LICENSE') as license_file:
    license = license_file.read()

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.readlines()

with open('requirements_dev.txt') as dev_requirements_file:
    test_requirements = dev_requirements_file.readlines()


setup(
    name='{{cookiecutter.project_slug}}',
    version='0.0.0',
    description="{{cookiecutter.project_short_description}}",
    long_description=readme,
    author="{{cookiecutter.full_name}}",
    author_email='{{cookiecutter.email}}',
    url='https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}',
    packages=[
        '{{cookiecutter.project_slug}}',
    ],
    include_package_data=True,
    install_requires=requirements,
    license=license,
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
