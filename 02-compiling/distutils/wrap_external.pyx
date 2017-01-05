# Import cfib.pxd
cimport cfib

cpdef int fib(int n):
    ''' Returns the nth Fibonacci number.'''
    return cfib.fib(n)
