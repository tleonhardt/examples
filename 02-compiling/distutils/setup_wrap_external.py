from setuptools import setup, Extension
from Cython.Build import cythonize

# First create an Extension object to wrap the external library
ext = Extension(name="wrap_external",
                sources=["wrap_external.pyx"],
                library_dirs=["."],
                libraries=["fib"])

# Use cythonize on the extension object.
setup(ext_modules=cythonize(ext))
