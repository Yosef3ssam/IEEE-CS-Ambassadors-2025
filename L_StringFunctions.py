n, q = map(int, input().split())
s = list(input().lower())
for _ in range(q):
    op = input().strip()
    if op == "pop_back":
        s.pop()
    elif op == "front":
        print(s[0])
    elif op == "back":
        print(s[-1])
    elif op == "sort":
        a, b = map(int, input().split())
        l, r = min(a, b) - 1, max(a, b)
        s[l:r] = sorted(s[l:r])
    elif op == "reverse":
        a, b = map(int, input().split())
        l, r = min(a, b) - 1, max(a, b)
        s[l:r] = s[l:r][::-1]
    elif op == "print":
        idx = int(input())
        print(s[idx - 1])
    elif op == "substr":
        a, b = map(int, input().split())
        l, r = min(a, b) - 1, max(a, b)
        print(''.join(s[l:r]))
    else:
        c = op
        s.append(c)
