#!/bin/python3
# coding: utf-8
"""
Convert tables in MD files to RST prior to processing by Sphinx.

.. warning::

    The script does not perform any tests on the conversion nor does it
    rollback if it encounters an error. Always check the rendered output.
    It is possible that some errors may occur that require manual fixes,
    especially when converting complex tables.

Borrowed from https://github.com/rackerlabs/docs-rackspace
"""

try:
    import configparser
except:
    import ConfigParser as configparser
import logging
from os import path, sep, walk
from shutil import copyfile

import pypandoc

numtables = 0  # number of tables converted during a run


def adjustrow(row):
    """
    Convert a grid row to a list-table row.

    :param row: a row of grid table text
    :type row: str
    :return: a row of list-table text
    :rtype: str
    """
    if row.startswith('+') is True:
        return('\n')
    row = row.split('|')
    new_row = []
    for entry in row:
        new_row.append(entry)
        try:
            new_row.pop(new_row.index(''))
        except:
            pass
    convert = []
    convert.append('   * - ' + new_row[0].strip())
    for entry in new_row[1:]:
        convert.append(('\n     - ' + entry.strip()).rstrip())
    result = ''.join(convert)
    return(result)


def buildtable(gridtable):
    """
    Build an RST list-table from an RST grid table.

    :param gridtable: an RST grid table
    :type gridtable: list
    :return: an RST list-table
    :rtype: str
    """
    col_num = gridtable[0].count('+') - 1
    col_width = str(int(100 / col_num))
    col_width = (' ' + col_width) * col_num

    output = []
    for line in gridtable:
        row = adjustrow(line)
        output.append(row)
    result = ''.join(output)
    list_table = """.. list-table::\n   :widths:%s\n   :header-rows: 1\n%s""" \
                 % (col_width, result)
    return(list_table)


def copydocs(files, tempsuffix):
    """
    Copy files for processing and move originals to temp filenames.

    :param files: list of filenames
    :type files: list
    :param temptsuffix: temporary file extension addition
    :type: str
    :returns: 0 (Success), 1 (Failure)
    :rtype: int
    :example:

    >>> copydocs(['file1.md.temp','file2.md.temp'], '.temp')
    1
    """
    try:
        for file in files:
            newfile = file + tempsuffix
            copyfile(file, newfile)
        return 0
    except Exception as e:
        logging.error('copydocs(): ' + str(e))
        return 1


def listfiles(docroot, suffix, ignore):
    """
    List docs with suffix extension in docroot directory.

    :param docroot: directory containing documentation files
    :type docroot: str
    :param suffix: extension of files to collect
    :type suffix: str
    :param ignore: file(s) to ignore
    :type ignore: str
    :returns: list of filenames in ``docroot`` with the ``suffix`` extension
    :rtype: list
    :example:

    >>> listfiles('./', '.none', 'README.md')
    []
    """
    ignore = ignore.split(',')
    ignore = tuple([x.strip() for x in ignore])
    docroot = path.realpath(docroot)
    filelist = []
    for subdir, dirs, files in walk(docroot):
        for file in files:
            filepath = subdir + sep + file
            if filepath.endswith(suffix) and not filepath.endswith(ignore):
                filelist.append(filepath)
    return(filelist)


def listtable(mdstring):
    """
    Process markdown string to convert grid tables to list-tables.

    :param mdstring: markdown string with RST grid tables
    :type mdstring: str
    :returns: markdown string with RST grid tables converted to RST list-tables
    :rtype: str
    """
    mdstring = mdstring.splitlines()
    grid = False
    insert = False
    gridtable = []
    content = []
    for line in mdstring:
        if line.startswith('+--') is True or line.startswith('+==') is True:
            grid = True
            insert = True
            gridtable.append(line)
        elif grid is True and line.startswith('|') is True:
            gridtable.append(line)
        else:
            grid = False
        if grid is False:
            if insert is True:
                insert = False
                newtable = buildtable(gridtable)
                content.append(newtable + '\n')
                gridtable = []
            else:
                content.append(line + '\n')
    content = ''.join(content)
    content = postparse(content)
    return(content)


def parsedoc(mdstring):
    """
    Find MD tables and convert them to RST grid tables.

    :param mdstring: markdown string with ``<!--table--> <!--endtable-->``
                     fenced tables
    :type mdstring: str
    :returns: markdown string with MD table converted to RST grid table
    :rtype: str
    :example:

    >>> parsedoc('A string of markdown.')
    'A string of markdown.'
    """
    output = []
    mdstring = preparse(mdstring)
    mdstring = mdstring.splitlines()
    start = False
    startmark = "<!--table-->"
    endmark = "<!--endtable-->"
    for line in mdstring:
        if line.startswith(startmark) is True:
            start = True
            table = ''
            output.append("```eval_rst")
        elif start is True and line.startswith(endmark) is False:
            table += line + "\n"
        elif start is True and line.startswith(endmark) is True:
            converted = pypandoc.convert(table, 'rst', format='md')
            output.append(converted + "\n```")
            start = False
            global numtables
            numtables += 1
        else:
            output.append(line)
    output = '\n'.join(output)
    return(output)


def preparse(mdstring):
    """
    Swap HTML tags for substitutes.

    :param mdstring: markdown string
    :type mdstring: str
    :returns: markdown string with HTML tags converted to parse-safe strings
    :rtype: str
    :example:

    >>> preparse('A string of <br />markdown.')
    'A string of @br@markdown.'
    """
    mdstring = mdstring.replace('<br />', '@br@')
    mdstring = mdstring.replace('<li>', '@li@')
    mdstring = mdstring.replace('</li>', '')
    return(mdstring)


def processdocs(files):
    """
    Convert tables in a list of docs using parsedoc() and listtable().

    :param files: files to process
    :type files: list
    :returns: 0 (Success), 1 (Failure)
    :rtype: int
    :example:

    >>> processdocs(['file1.md.temp','file2.md.temp'])
    1
    """
    try:
        for file in files:
            doc = readfile(file)
            result = parsedoc(doc)
            writefile(file, result)
            doc = readfile(file)
            result = listtable(doc)
            writefile(file, result)
        return 0
    except Exception as e:
        logging.error('Process docs error (processdocs): ' + str(e))
        return 1


def postparse(mdstring):
    r"""
    Swap HTML substitutes for strings.

    :param mdstring: markdown string
    :type mdstring: str
    :returns: markdown string with parse-safe substitutes converted to strings
    :rtype: str
    :example:

    >>> postparse('A string of @br@markdown.')
    'A string of \n      markdown.'
    """
    mdstring = mdstring.replace('@br@@br@', '\n\n      ')
    mdstring = mdstring.replace('@br@', '\n      ')
    mdstring = mdstring.replace('@li@', '\n       - ')
    return(mdstring)


def readfile(infile):
    """
    Read data from file and return text as a string.

    :param infile: file to read
    :type infile: str
    :returns: text (Success), 1 (Failure)
    :rtype: str or int
    :example:

    >>> readfile('tools/example.txt')
    'Hello world!'
    """
    try:
        infile = path.realpath(infile)
        with open(infile, 'r') as f:
            data = f.read()
        return(data)
    except Exception as e:
        logging.error('Read error (readData): ' + str(e))
        return 1


def writefile(outfile, data):
    """
    Write data to file.

    :param outfile: file to write
    :type files: str
    :returns: 0 (Success), 1 (Failure)
    :rtype: int
    :example:

    >>> writefile('tools/example.txt', 'Hello world!')
    0
    """
    try:
        outfile = path.realpath(outfile)
        with open(outfile, 'w') as f:
            f.write(data)
        return 0
    except Exception as e:
        logging.error('Write error (writeData): ' + str(e))
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
    files = listfiles(conf['docdir'], conf['mdsuffix'], conf['ignore'])
    copydocs(files, conf['tempsuffix'])
    processdocs(files)
    print('Tables converted: ' + str(numtables))
