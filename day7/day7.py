import copy
import sys
from functools import lru_cache

# Recursively compute the number of ways to go from a position by calling the function twice on itself at every '^' and stopping when hitting the bottom
# Additionally uses a memoization cache to speed up already calculated positions
@lru_cache(None)
def quantum_count(row, col):
    global lines
    if row == len(lines)-1:
        return 1
    if lines[row][col] == '^':
        return quantum_count(row+1, col-1) + quantum_count(row+1, col+1)
    else:
        return quantum_count(row+1, col)


# Read input and configure for part A
lines = []
with open("input.txt", 'r') as f:
    for line in f.readlines():
        lines.append(list(line.strip()))

start = -1
for i in range(len(lines[0])):
     if lines[0][i] == 'S':
            lines[0][i] = '|'
            start = i

count_a = 0
count_b = quantum_count(1, start)

# Draw light path, splitting at '^' 
for row in range(1, len(lines)):
     for col in range(len(lines[0])):
          if lines[row-1][col] == '|':
               if lines[row][col] == '^':
                    count_a += 1
                    lines[row][col-1] = '|'
                    lines[row][col+1] = '|'
               else:
                    lines[row][col] = '|'
                
print("Part A:", count_a)
print("Part B:", count_b)