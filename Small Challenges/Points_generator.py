"""
The goal is to create a pattern based on a certain radius (58 in this case) to optimize the area.
because the limits of the areas are irregular, and to utilize as much area as possible,
the construction of the path will be done line by line.
"""

import math
import os


def write_point():
    with open(path, 'a') as file:
        file.write(f'{begin}, {lon}, {lat}, {rest[0]}, {rest[1]}\n')


start = input('Copy the starting point: ') # ex: 'Country', 1000, 1000, 141, Location
start = start.replace(' ', '')
start = start.split(',')

begin, lon, lat, *rest = start
lat = int(lat)
lon = int(lon)

direction = input('Witch way should be the path? [N, S, E, W] ').upper()
direction2 = input('Witch way should be the lines? [N, S, E, W] ').upper()

file_direct = input('what is the file directory? ')
path = os.path.abspath(file_direct)

new_line = True

while new_line:
    end = int(input('what is the maximum coordinate? '))
    if direction == 'N':
        while lat < end:
            write_point()
            lat += 116
    elif direction == "S":
        while lat > end:
            write_point()
            lat -= 116
    elif direction == 'E':
        while lon < end:
            write_point()
            lon += 116
    elif direction == 'W':
        while lon > end:
            write_point()
            lon -= 116

    next_line = input('Do you want to create a new line? [Y, N]').upper()
    if next_line == 'Y':
        nl_star = int(input('what is the starting coordinate? '))

        if direction2 == 'E':
            lon += 101
        elif direction2 == 'W':
            lon -= 101
        elif direction2 == 'N':
            lat += 101
        else:
            lat -= 101

        if direction == 'N':
            direction = 'S'
            lat += 58 + math.floor((nl_star - lat)/116)*116
        elif direction == 'S':
            direction = 'N'
            lat += 58 + math.floor((nl_star - lat)/116)*116

        elif direction == 'E':
            direction = 'W'
            lon += 58 + math.floor((nl_star - lon)/116)*116

        elif direction == 'W':
            direction = 'E'
            lon += 58 + math.floor((nl_star - lon)/116)*116

        continue
    new_line = False
