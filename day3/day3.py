with open("input.txt", 'r') as f:
    lines = f.readlines()

sum_a = 0
sum_b = 0

for line in lines:
    line = line.strip()
    
    # Initialize arrays to contain the optimal voltages
    top_a = [0,0]
    top_b = [0 for i in range(12)]

    # Iterate through each bank
    for j in range(len(line)):
        val = int(line[j])

        # Compare current value to top n
        for i in range(len(top_a)):
            # Skip if placing the value in the top nth spot would not leave enough space for the rest of the top n to be filled from remaining values
            if len(line) - (j+1) < len(top_a) - (i+1):
                    continue
            
            # Replace the top nth spot that current value beats and reset the n+1 top spot to 0 as that value is no longer valid because it came from before the value higher
            # Because we do not replace spots that won't be able to be filled by future input, this 0 will be replaced on the next input read and 0 will pass through all top 
            # n spots
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

    # Calculate voltage from optimal top values
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