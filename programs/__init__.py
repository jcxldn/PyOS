from importlib import import_module as __import_module
from os import path as __path

import glob as __glob

__modules = __glob.glob(__path.join(__path.dirname(__file__), "*.py"))
__files = [ __path.basename(__f)[:-3] for __f in __modules if __path.isfile(__f) and not __f.endswith('__init__.py')]

for __i in __files:
    __import_module('.' + __i, __name__)