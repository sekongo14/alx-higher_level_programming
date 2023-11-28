#!/usr/bin/python3
def remove_char_at(str, n):
    char = str[:n-1]+ str[n:]
    return char
