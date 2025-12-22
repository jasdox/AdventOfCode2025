with open("input.txt", 'r') as f:
    lines = f.readlines()

dial = 50
count_a = 0
count_b = 0

for line in lines:
    # Read input
    line = line.strip()
    direction = line[0]
    distance = int(line[1:])

    # Modify sign of distance by direction
    if direction == 'L':
        distance *= -1
    # If dial will pass 99 to the right, increment count_b for every pass
    while dial + distance > 100:
        distance -= (100 - dial)
        dial = 0
        count_b += 1
    # If dial will pass 0 to the left, and didn't start on 0, increment count_b for every pass
    while dial + distance < 0:
        distance += ((dial+1))
        if dial != 0:
            count_b += 1
        dial = 99

    # Dial will not pass either side so check if it lands exactly on 0 and increment count_a
    dial += distance 
    if dial % 100 == 0:
        count_a += 1
        count_b += 1
        dial = 0

print("Part A:", count_a)
print("Part B:", count_b)