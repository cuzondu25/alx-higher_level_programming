#!/usr/bin/python3
def uppercase(str):
    str = str + "\n"
    for x in str:
        if ord(x) >= 97 and ord(x) <= 122:
            print("{}".format(chr(ord(x) - 32)), end="")
        else:
            print("{}".format(x), end="")
