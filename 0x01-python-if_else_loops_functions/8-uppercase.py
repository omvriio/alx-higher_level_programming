#!/usr/bin/python3
def uppercase(str):
    if ord(str) >= 97:
        print(chr(ord(str) - 32))
    else:
        print(str)
