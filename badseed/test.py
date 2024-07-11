#!/usr/bin/env python3

from ctypes import CDLL

libc = CDLL("libc.so.6")
s = libc.time(0)
libc.srand(s)
#print("Current time is: %d" % s)
print(libc.rand())

