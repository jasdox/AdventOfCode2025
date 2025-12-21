with open("input.txt", 'r') as f:
    lines = f.readlines()

for i in range(len(lines)):
    line = lines[i]
    line = line.strip()
    line = "." + line + "."
    line = list(line)
    lines[i] = line

lines.insert(0, ["." for j in range(len(lines[0]))])
lines.insert(len(lines)+1, ["." for j in range(len(lines[0]))])


count_a = 0
count_b = 0

locations = []

# Part A
for row in range(len(lines)):
    for col in range(len(lines[0])):
        if lines[row][col] == '@':
            locations.append((row,col))
            adj_count = 0
            for i in range(row-1, row+2):
                for j in range(col-1, col+2):
                    if lines[i][j] == '@':
                        adj_count += 1
            if adj_count <= 4:
                count_a += 1

# Part B
while True:
    new_locations = []
    changed = False
    for k in range(len(locations)):
            row, col = locations[k]
            removed = []
            if lines[row][col] == '@':
                adj_count = 0
                for i in range(row-1, row+2):
                    for j in range(col-1, col+2):
                        if lines[i][j] == '@':
                            adj_count += 1
                if adj_count <= 4:
                    count_b += 1
                    lines[row][col] = '.'
                    changed = True
                else:
                    new_locations.append((row,col))
    if not changed:
        break
    locations = new_locations

print("Part A:", count_a)
print("Part B", count_b)