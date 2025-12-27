with open(r"day1input.txt", 'r') as file:
    lines = file.readlines()

def part1():
    position = 50
    count = 0

    for line in lines:

        dir = line[0]
        val = int(line[1:])

        if dir == 'R':
            position = (position + val) % 100
        else:
            position = (position - val)  % 100
            
        if position == 0:
            count += 1
    return count

#Part 2
def part2():
    position = 50
    count = 0

    for line in lines:

        dir = line[0]
        val = int(line[1:])

        full, partial = divmod(val, 100)
        count += full

        delta = partial if dir == 'R' else -partial
        new_pos = position + delta

        if position != 0:
            if dir == "L" and new_pos <= 0:
                count += 1
            elif dir == "R" and new_pos >= 100:
                count += 1

        position = new_pos % 100
    return count


print(part1)
print(part2)
