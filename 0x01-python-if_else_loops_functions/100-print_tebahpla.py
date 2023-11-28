#!/usr/bin/python3
def print_reverse_alphabet():
    for i in range(ord('z'), ord('a') - 1, -1):
        print("{}".format(chr(i).lower()) if i % 2 == 0 else "{}".format(chr(i).upper()), end="")


print_reverse_alphabet()
