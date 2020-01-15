#!/usr/bin/env python3
name = input("please enter file name: ")
fobj = open(name)
print(fobj.read())
fobj.close()
