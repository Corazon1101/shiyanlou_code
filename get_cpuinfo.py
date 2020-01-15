#!/usr/bin/env python3
import os
import sys
if len(sys.argv) < 1:
    print("wrong parameter")
else:
    with open(sys.argv[1]) as f1:
        for line in f1:
            print(line)
