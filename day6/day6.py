sum_a = 0
i = 0

# Part A

while True:
    nums = []
    op = ''

    with open("input.txt", 'r') as f:
        for line in f:
            try:
                num = line.strip().split()[i]
                nums.append(num)
            except IndexError:
                pass

    if not nums:
        break

    op = nums.pop(-1)

    if op == "+":
        sum_temp = 0
        for num in nums:
            sum_a += int(num)

    else:
        product_temp = 1
        for num in nums:
            product_temp *= int(num)
        sum_a += product_temp

    
    i += 1

print("Part A:", sum_a)


# Part B

sum_b = 0
i = 0
op = ''

while True:
    nums = []
    with open("input.txt", 'r') as f:
        for line in f:
                try:
                    num = line[i]
                    nums.append(num)
                except IndexError:
                    pass

    if not nums:
        break

    if nums[-1] != ' ' and nums[-1] != '\n':
        op = nums.pop(-1)
        if op == "+":
            ans = 0
        else:
            ans = 1
    else:
        nums.pop(-1)

    if len(''.join(nums).strip()) == 0:
        sum_b += ans
        ans = 0
        if op == "*":
            ans = 1
        i += 1
        continue
        
    if op == "+":
        temp_str = ''

        for num in nums:
            temp_str += num
        ans += int(temp_str)
    else:
        temp_str = ''
        for num in nums:
            temp_str += num
        ans *= int(temp_str)
    
    i += 1

print("Part B:", sum_b)