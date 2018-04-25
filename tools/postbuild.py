#!/bin/python3
# coding: utf-8
"""
Remove temp files created by prebuild and rename original files.

Borrowed from https://github.com/rackerlabs/docs-rackspace
"""

try:
    import configparser
except:
    import ConfigParser as configparser
import logging
from os import path, rename
from prebuild import listfiles


def cleanup(files, tempsuffix):
    """
    Revert source files and remove temp files.

    :param files: files with ``.temp`` extension
    :type files: list
    :param temptsuffix: temporary file extension addition
    :type: str
    :returns: 0 (Success), 1 (Failure)
    :rtype: int
    :example:

    >>> cleanup(['file1.md.temp','file2.md.temp'], '.temp')
    0

    """
    logging.debug('Running cleanup()')
    try:
        for file in files:
            if path.exists(file):
                rename(file, file[:-len(tempsuffix)])
        return 0
    except Exception as e:
        logging.error('Cleanup error (cleanup): ' + str(e))
        return 1


if __name__ == '__main__':
    conf = {
        'docdir': "./",
        'mdsuffix': ".md",
        'tempsuffix': ".temp",
        'ignore': "None",
        'debug': True
    }
    if conf['debug'] == 'True':
        logging.basicConfig(level=logging.DEBUG)
    files = listfiles(conf['docdir'], conf['tempsuffix'], conf['ignore'])
    result = cleanup(files, conf['tempsuffix'])
    if result == 0:
        print('Cleanup complete.')
    else:
        print('Cleanup failed.')
