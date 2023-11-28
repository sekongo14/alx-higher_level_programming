#!/usr/bin/python3
def islower(c):
    fr = ord(c)
    if fr >= ord("a") and fr <= ord("z"):
        return True
    else:
        return False
