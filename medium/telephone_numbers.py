import sys
import math
import collections

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

tree = lambda: collections.defaultdict(tree)
stash = tree()
number = 0

n = int(input())
for i in range(n):
    stored = stash
    telephone = input()
    for k in telephone:
        if k not in stored:
            number += 1
        stored = stored[k]

# The number of elements (referencing a number) stored in the structure.
print(number)
