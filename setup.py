#!/usr/bin/env python

from setuptools import setup, find_packages
import os

MAJOR = 0
MINOR = 0
MICRO = 1
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)

setup_dir = os.path.abspath(os.path.dirname(__file__))
readme_file = os.path.join(setup_dir, 'README.md')

try:
    from m2r import parse_from_file
    README = parse_from_file(readme_file)
except ImportError:
    # m2r may not be installed in user environment
    with open(readme_file) as f:
        README = f.read()

def write_version_py(filename=os.path.join(setup_dir, 'feature_customer/version.py')):
    version = VERSION
    a = open(filename, 'w')
    file_content = "\n".join(["",
                              "# THIS FILE IS GENERATED FROM SETUP.PY",
                              "version = '%(version)s'",
                              "isrelease = '%(isrelease)s'"])

    a.write(file_content % {'version': VERSION,
                            'isrelease': "True"})
    a.close()

write_version_py()

NAME = "simple_recipes"

DESCRIPTION = ("Simple preprocessing pipelines for vanilla Python")
KEYWORDS = "simple recipes"
AUTHOR = "Chapman Siu"
AUTHOR_EMAIL = "chapm0n.siu@gmail.com"
URL = 'chappers.github.io'

extras_require = {'development': ['nose2>=0.7.4',
                                  'coverage>=4.5.1',
                                  'nose2_html_report>=0.6.0',
                                  'sphinxcontrib-napoleon>=0.6.1',
                                  'pandoc>=1.0.2',
                                  'nbsphinx>=0.3.3',
                                  'flake8>=3.5.0',
                                  'awscli>=1.15.26',
                                  'future>=0.16.0',
                                  'm2r']
                    }
extras_require['complete'] = sorted(set(sum(extras_require.values(),[])))

setup(
    name = NAME,
    version = VERSION,
    description = DESCRIPTION,
    long_description=README,
    keywords = KEYWORDS,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    url = URL,
    packages =find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires = INSTALL_REQUIRES,
    extras_require = extras_require,
    zip_safe=False # force install as source
)
