#!/usr/bin/env python

from distutils.core import setup
from os.path import dirname

setup(name='vcf',
      version='0.1.0',
      description='feed classifier script',
      author='Nyiro, Gergo',
      author_email='gergo.nyiro@gmail.com',
      py_modules=['vcard'],
      package_dir = {'': 'lib'},
      scripts=['bin/vdown'],
      license=open(dirname(__file__)+'/LICENSE').read(),
      url='https://github.com/nyirog/vcf',
 )

