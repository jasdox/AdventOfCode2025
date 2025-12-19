with open("input.txt", 'r') as f:
    lines = f.readlines()

dial = 50
count_a = 0
count_b = 0

for line in lines:
    line = line.strip()
    direction = line[0]
    distance = int(line[1:])

    if direction == 'L':
        distance *= -1
    while dial + distance > 100:
        distance -= (100 - dial)
        dial = 0
        count_b += 1
    while dial + distance < 0:
        distance += ((dial+1))
        if dial != 0:
            count_b += 1
        dial = 99

    dial += distance 
    if dial % 100 == 0:
        count_a += 1
        count_b += 1
        dial = 0

print("Part A:", count_a)
print("Part B:", count_b)