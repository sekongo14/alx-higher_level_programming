#!/usr/bin/python3
def remove_char_at(str, n):
    if n == 0:
        char = str[1:]
    elif n > 0:
        char = str[:n] + str[n+1:]
    else:
        char = str[:n] + str[n:]
    return char
