all:
	# Compile cfib.c with position-independent code
	gcc -std=c11 -c -Wall -Werror -g0 -O3 -fpic cfib.c

	# Create a shared library from an object file
	gcc -shared -o libfib.so cfib.o

	# Build the Cython code using setuptools
	python setup.py build_ext --inplace

	# Build the Cython wrapper around C code using setuptools
	python setup_wrap.py build_ext --inplace

	# Build the Cython wrapper around external dynamic library
	python setup_wrap_external.py build_ext --inplace

clean:
	rm -rf build fib.c wrap_fib.c *.so
