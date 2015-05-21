# python_tools

A set of python tools that I've made to scratch itches.

## is_pdf.py

*Now with the ability to be imported as a module!*

    >>> import is_pdf
    >>> is_pdf.isPdfOpen("/Users/scottmmjackson/14-1799.Opinion.5-19-2015.1.PDF")
    True
    >>> is_pdf.isPdfOpen("/Users/scottmmjackson/14-1799.Opinion.5-19-2015.1.html")
    False

is_pdf.isPdf(filehandle) - takes a filehandle and returns true or false

is_pdf.isPdfOpen(filename) - takes a fully qualified file name and passes the return value from isPdf

For command-line usage, pass --help to is_pdf.py.