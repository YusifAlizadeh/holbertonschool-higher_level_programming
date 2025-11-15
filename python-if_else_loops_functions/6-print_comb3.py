#!/usr/bin/python3
for i in range(9):
    for j in range(i + 1, 10):
        print(f"{i}{j}", end=", " if j < 9 or i < 8 else "\n")
