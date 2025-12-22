with open("input.txt", 'r') as f:
    lines = f.readlines()

# Add padding around input so all surrounding values can be searched
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

# Initalize array to store locations of paper rolls
locations = []

# Part A
# Search through grid until finding a roll and count rolls around that roll to determine if it is removable
for row in range(len(lines)):
    for col in range(len(lines[0])):
        if lines[row][col] == '@':
            locations.append((row,col))  # Remember where paper rolls are located 
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
    # Search through only locations discovered during part a
    for k in range(len(locations)):
            row, col = locations[k]
            removed = []
            # If roll is removable, replace it in the grid and increment counter
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
                    new_locations.append((row,col)) # update locations to contain only rolls that haven't been removed yet
    if not changed: # Stop searching when no changes are made after searching entire grid
        break
    locations = new_locations

print("Part A:", count_a)
print("Part B", count_b)