#!/usr/bin/python3
for letter in "abcdefghijklmnopqrstuvwxyz":
    print("{0}".format(letter), end='') if letter not in 'eq' else None
