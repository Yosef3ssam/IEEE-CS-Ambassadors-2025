def both():
    n = int(input())
    a = list(map(int,input().split()))
    min = a[0]
    max = a[0]
    for i in range(len(a)):
        if max < a[i]:
            max = a[i]
        if min > a[i]:
            min = a[i]
    return min , max

last = both()
print(' '.join(map(str, last)))
