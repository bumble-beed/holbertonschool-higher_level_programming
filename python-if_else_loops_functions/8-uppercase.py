#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i.str) >= 97 and ord(i.str) <= 122:
            c = chr(ord(i) - 32)
            print("{}".format(i), end="")
