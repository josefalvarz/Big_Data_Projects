#!/usr/bin/env python3
import sys

# This reducer just forwards the mapper output line by line
for line in sys.stdin:
    print(line.strip())
