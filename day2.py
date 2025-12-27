with open(r"day2input.txt", 'r') as file:
    ranges = file.read().split(',')


#PART1
def part1():
    def invalid(x):
        x = str(x)
        return len(x)%2 == 0 and x[:len(x)//2] == x[len(x)//2:]

    ans = 0
    for i in ranges:
        first, last = i.split('-')
        first = int(first)
        last = int(last)
        for x in range(first, last + 1):
            if invalid(x):
                ans += x
    return ans

#PART2
def part2():
    def invalid(x):
        x = str(x)
        return x in (x+x)[1:-1]

    ans = 0
    for i in ranges:
        first, last = i.split('-')
        first = int(first)
        last = int(last)
        for x in range(first, last + 1):
            if invalid(x):
                ans += x
    return ans

print(part1())
print(part2())

