ranges = []
ingredients = []

in_ranges = True

# Read input and seperate ranges from ingredients
with open("input.txt", 'r') as f:
    for line in f:
        line = line.strip()
        if line == "":
            in_ranges = False
            continue
        if in_ranges:
            line = line.split('-')
            line = [int(line[i]) for i in range(len(line))]
            ranges.append(line)
        else:
            ingredients.append(int(line))

# sort ranges and ingredients
ranges = sorted(ranges)
ingredients = sorted(ingredients)

# merge adjacent ranges if the end of the first and start of the next overlap
i = 1
while i < len(ranges):
    if ranges[i][0] <= ranges[i-1][1]:
        ranges[i-1][1] = max(ranges[i-1][1], ranges[i][1])
        ranges.pop(i)
    else:
        i += 1

count_a = 0

range_idx = 0
ing_idx = 0

# Iterate through ingredients until above the current range, then move to next range and repeat, counting fresh ingredients
while ing_idx < len(ingredients):
    r = ranges[range_idx]
    num = ingredients[ing_idx]
    if num >= r[0] and num <= r[1]:
        count_a += 1
        ing_idx += 1
    elif num > r[1] and range_idx < (len(ranges)-1):
        range_idx += 1
    else:
        ing_idx += 1

print("Part A:", count_a)

# Count values between all merged ranges
count_b = 0
for r in ranges:
    count_b += len(range(r[0], r[1]+1))


print("Part B:", count_b)