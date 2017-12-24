import sys
import math

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
grid = []

for i in range(height):
    line = input()  # width characters, each either 0 or .
    grid.append(list(line))


for j in range(height):
    for i in range(width):
        if grid[j][i] == '0':
            x1, y1 = i, j
            x2, y2 = -1, -1
            x3, y3 = -1, -1

            # right horizontal  neighbour
            for k in range(i + 1, width):
                if grid[j][k] == '0':
                    x2, y2 = k, j
                    break

            # vertical neighbors
            for k in range(j + 1, height):
                if grid[k][i] == '0':
                    x3, y3 = i, k
                    break

            print(x1, y1, x2, y2, x3, y3)
