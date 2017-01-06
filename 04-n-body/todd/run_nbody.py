#!/usr/bin/env python
import sys
from nbody import main

# Number of iterations to run the N-body simulation forl
N = 500000
if len(sys.argv) > 1:
    N = int(sys.argv[1])

main(N)
