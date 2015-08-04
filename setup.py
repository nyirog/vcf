#!/usr/bin/env python

from distutils.core import setup
from os.path import dirname, abspath

setup(name='vcf',
      version='0.1.0',
      description='feed classifier script',
      author='Nyiro, Gergo',
      author_email='gergo.nyiro@gmail.com',
      packages=['vcard'],
      package_dir = {'': 'lib'},
      scripts=['bin/vdown'],
      license=open(dirname(abspath(__file__))+'/LICENSE').read(),
      url='https://github.com/nyirog/vcf',
 )

