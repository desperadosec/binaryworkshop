#!/usr/bin/env python3

from pwn import *

io = process('sh')
io.sendline(b'echo Hello, world')
a = io.recvline()
print(a)

