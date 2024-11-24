#!/usr/bin/python3
with open('thrust.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

with open('new_thrust', 'w', encoding='utf-8') as file:
    for i, line in enumerate(lines):
        if (i + 1) % 3 == 0:
            file.write(line)
