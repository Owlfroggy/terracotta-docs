#!/usr/bin/env python
from setuptools import setup, find_packages

entry_points = '''
[pygments.lexers]
terracotta=terracotta_lexer:TerracottaLexer
'''

setup(
    name='terracotta-docs',
    version='1.0', #probably meaningless version number
    packages=find_packages(),
    entry_points=entry_points,
)
