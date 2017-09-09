"""
Support functions, mainly for Pythonic things (like compatibility 2/3)
"""
import sys
import logging
import inspect
import os


def merge_two_dicts(x, y):
    """ Given two dicts, merge them into a new dict as a shallow copy.
    https://stackoverflow.com/questions/38987/how-to-merge-two-dictionaries-in-a-single-expression"""
    if (sys.version_info > (3, 4)):
        # z = {**x, **y}     # Find out how to leave this code valid in Py2 and Py3
        z = x.copy()        # Delete these 3 lines if solved
        z.update(y)			 #
        return z			 #
    else:
        # Python  < 3.5
        z = x.copy()
        z.update(y)
        return z


def log_bulk(level, *args):
    func = inspect.currentframe().f_back.f_back
    filename = os.path.basename(func.f_code.co_filename)
    funcname = func.f_code.co_name
    lineno = func.f_lineno
    for msg in args:
        logging.log(level, "{:>15} - {:>4} - {:>20} | {}".format(filename, lineno, funcname, msg))

def debug_bulk(*args):
    log_bulk(getattr(logging, "DEBUG"), *args)
