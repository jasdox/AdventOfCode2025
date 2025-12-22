# Read input and seperate into ranges
with open("input.txt", 'r') as f:
    input = f.read().strip().split(",")

sum_a = 0
sum_b = 0

# Format input 
for i in range(len(input)):
    input[i] = input[i].split("-")
    input[i][0] = int(input[i][0])
    input[i][1] = int(input[i][1])

for pair in input:
    # Iterate through all ranges 
    for i in range(pair[0], pair[1] + 1):
        # Split id in half and check equivalence
        string = str(i)
        s1 = string[:int(len(string)/2)]
        s2 = string[int(len(string)/2):]

        if s1 == s2:
            sum_a += i

        # Detect any repition in string by concatonating the string with itself and testing if the original string spans the gap between the concatonations
        if string in (string + string)[1:-1]:
            sum_b += i

print("Part A:", sum_a)
print("Part B:", sum_b)