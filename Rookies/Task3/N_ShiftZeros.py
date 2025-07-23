def zero ():
    n = int(input())
    a = list(map(int,input().split()))
    real = []
    for i in a:
        if i != 0:
            real.append(i)
    zero_count = n - len(real)
    for _ in range(zero_count):
        real.append(0)
    return real
print(" ".join(map(str,zero())))