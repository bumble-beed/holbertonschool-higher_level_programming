#!/usr/bin/python3
def uppercase(str):
    for i in str:
        c = chr(ord(i) - 32)
        return ord(str) >= 65 and ord(c) <= 90
