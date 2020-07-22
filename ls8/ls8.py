#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

if len(sys.argv) < 2:
    print("Please enter the file path of a program to run.")
    sys.exit(1)

l = []
try:
    with open(sys.argv[1]) as file:
        for line in file:
            l.append(line)
    print(1) # is this like print(true)?

except FileNotFoundError:
    print(f"{sys.argv[0]}: {sys.argv[1]} not found!")
    sys.exit(2) # what this means?



cpu = CPU()

cpu.load()
cpu.run()