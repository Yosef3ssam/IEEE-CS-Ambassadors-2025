def calc(x, y):
    s = 0
    for i in range(2, y + 1, 2):
        power = 1
        for _ in range(i):
            power *= x
        s += power
    return s

x, y = map(int, input().split())
result = calc(x, y)
print(result)
