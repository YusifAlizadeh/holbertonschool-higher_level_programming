#!/usr/bin/python3
def islower(c):
    if ord(c) in [ord(i) for i in 'abcdefghijklmnopqrstuvwxyz']:
        return True
    else:
        return False
