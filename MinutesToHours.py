#!/usr/bin/env python3
import sys

def Hours(m):
    H = m // 60
    M = m % 60
    return H, M


def Main(m):
    hours, minutes = Hours(m)
    if m >= 0:
        print("{} H, {} M".format(hours, minutes))
        return True
    else:
        raise ValueError("Input number cannot be negative")
        return False


if __name__ == '__main__':
    try:
        Main(int(sys.argv[1]))
    except:
        print("Parameter Error")
