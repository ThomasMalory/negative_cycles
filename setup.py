"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='negative_cycles',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.1.0',

    description='A sample Python project',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/mnpatil17/negative-cycles/',

    # Author details
    author='Mihir Patil',
    author_email='mnpatil17@gmail.com',

    # Choose your license
    license='BSD 3-clause "New" or "Revised License"',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: BSD License',

        'Programming Language :: Python :: 2.7',
    ],

    # What does your project relate to?
    keywords='negative-cycle bellman-ford',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['numpy', 'nose'],

    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
)