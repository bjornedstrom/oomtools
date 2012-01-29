#!/usr/bin/env python

from distutils.core import setup

setup(name='oomtools',
      version='0.1.0',
      description='Tools for administrating the Linux kernel OOM killer.',
      author='Bjorn Edstrom',
      author_email='be@bjrn.se',
      url='https://github.com/bjornedstrom/oomtools',
      scripts=['oomps', 'oomset'],
     )
