s = input()
target = 'hello'
i = 0

for c in s:
    if c == target[i]:
        i += 1
        if i == len(target):
            break
if i == len(target):
    print('YES')
else:
    print('NO')