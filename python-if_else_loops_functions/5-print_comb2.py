#!/usr/bin/python3

# print numbers 9 to 99 with , separating them and 2 decimal places
for i in range(0, 100):
    if i == 99:
        print("{:02d}".format(i))
    else:
        print("{:02d}".format(i), end=", ")
