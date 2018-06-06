# -*- encoding:utf-8 -*-

import logging
# import os
from os import path

logging.basicConfig(level=logging.DEBUG)
debug = logging.debug

__author__ = 'LY'

'''
    extension for path
'''


def resolve(pkg_path, relative_path):
    return path.normpath(path.join(path.dirname(pkg_path), relative_path))


def main():
    print(path.normpath(path.join(__file__, "../../static/musics")))



if __name__ == '__main__':
    main()
