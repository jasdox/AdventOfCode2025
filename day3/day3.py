with open("input.txt", 'r') as f:
    lines = f.readlines()

sum_a = 0
sum_b = 0

for line in lines:
    line = line.strip()
    top_a = [0,0]
    top_b = [0 for i in range(12)]
    for j in range(len(line)):
        val = int(line[j])
        for i in range(len(top_a)):
            if len(line) - (j+1) < len(top_a) - (i+1):
                    continue
            if val > top_a[i]:
                top_a[i] = val
                if (i+1) != len(top_a):
                    top_a[i+1] = 0
                break
        for i in range(len(top_b)):
            if len(line) - (j+1) < len(top_b) - (i+1):
                    continue
            if val > top_b[i]:
                top_b[i] = val
                if (i+1) != len(top_b):
                    top_b[i+1] = 0
                break
    joltage = ""
    for num in top_a:
         joltage += str(num)
    sum_a += int(joltage)

    joltage = ""
    for num in top_b:
         joltage += str(num)
    sum_b += int(joltage)

    
print("Part A:", sum_a)
print("Part B:", sum_b)