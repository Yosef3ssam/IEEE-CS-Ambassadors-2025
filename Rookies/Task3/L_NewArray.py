def array():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    all = b + a
    return ' '.join(map(str, all))
print(array())