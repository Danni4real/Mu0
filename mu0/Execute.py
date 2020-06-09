#!/usr/bin/python3

import sys
from Mu0 import *
from Mem import *
from Timer import *
from Loader import *

mu0_init()
load_mem_image(load_bin(sys.argv[1]))
timer()
