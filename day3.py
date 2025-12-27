with open(r"day3input.txt") as file:
    '''#Part 1
    total_joltage = 0

    for line in file:
        line = line.strip()

        first = max(line[:-1])
        second = max(line[line.find(first)+1:])
        total_joltage += int(first + second)
    '''
    # Part 2
    total_joltage = 0
    for line in file:
        start = 0
        joltage = ""
        for i in reversed(range(12)):
            value = max(line[start:-i])
            start = line.find(value, start) + 1
            joltage += value
        total_joltage += joltage
        
print(total_joltage)
