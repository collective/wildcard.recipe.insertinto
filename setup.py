# -*- coding: utf-8 -*-
"""
This module contains the tool of wildcard.recipe.insertinto
"""
import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '1.0a1'

long_description = (
    read('README.txt')
    + '\n' +
    read('CHANGES.txt')
    )
entry_point = 'wildcard.recipe.insertinto:Recipe'
entry_points = {"zc.buildout": ["default = %s" % entry_point]}

tests_require = ['zope.testing', 'zc.buildout']

setup(name='wildcard.recipe.insertinto',
      version=version,
      description="allow you to insert text into files",
      long_description=long_description,
      classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Zope Public License',
        ],
      keywords='buildout insert file',
      author='Nathan Van Gheem',
      author_email='nathan.vangheem@wildcardcorp.com',
      url='',
      license='ZPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['wildcard', 'wildcard.recipe'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'zc.buildout'
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite='wildcard.recipe.insertinto.tests.test_docs.test_suite',
      entry_points=entry_points,
      )
