#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', 'scipy', 'numpy', 'matplotlib', 'imageio']

test_requirements = ['pytest>=3', ]

setup(
    author="Nipun Waas",
    author_email='waasnipun@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="An algorithm visualization pip package for Python",
    entry_points={
        'console_scripts': [
            'artific=artific.cli:main',
        ],
    },
    long_description_content_type='text/markdown',
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='artific',
    name='artific',
    packages=find_packages(include=['artific', 'artific.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/waasnipun/artific',
    version='0.0.9',
    zip_safe=False,
)
