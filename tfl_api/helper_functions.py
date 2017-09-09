"""
Support functions, mainly for Pythonic things (like compatibility 2/3)
"""
import sys

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
