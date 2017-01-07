# distutils: language=c++

from libcpp.vector cimport vector
from libcpp.string cimport string
from libcpp.map cimport map
from libcpp.pair cimport pair

def foobar():
    cdef vector[string] cpp_strings = b'ab cd ef gh'.split()
    return cpp_strings

def periodic_table_orig():
    """Demonstrates the manual way to build up a
    std::map in Cython.
    """
    cdef map[string, int] table
    cdef pair[string, int] entry
    # Insert Hydrogen
    entry.first = b"H"; entry.second = 1
    table.insert(entry)
    # Insert Helium
    entry.first = b"He"; entry.second = 2
    table.insert(entry)
    return table


def periodic_table():
    cdef map[string, long] table
    # NOTE: You can auto-convert from dictionary to map, but need a Python object, not literal
    table_dict = {b"H": 1, b"He": 2, b"Li": 3}
    table = table_dict
    # ...use table in C++...
    return table
