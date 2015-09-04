import os
import sys

import task

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.md', 'r', 'utf-8') as fp:
    long_description = fp.read()
    
packages = ['task', 'task.job', 'task.trigger']

classifiers = [
               'Intended Audience :: Developers',
               'Development Status :: 5 - Production/Stable',
               'Intended Audience :: Developers',
               'Natural Language :: English',
               'License :: OSI Approved :: Apache Software License',
               'Programming Language :: Python',
               'Programming Language :: Python :: 2.6',
               'Programming Language :: Python :: 2.7',
               'Topic :: Software Development :: Libraries',
               'Topic :: Utilities'
]

setup(
      name = 'py-task',
      version = task.__version__,
      author = 'Yugeng Hui',
      author_email = 'interhuiyg@163.com',
      url = 'https://github.com/interhui/py_task',
      packages = packages,
      description = 'Task scheduling tools for python',
      long_description = long_description,
      license = 'Apache 2.0',
      classifiers = classifiers
)
