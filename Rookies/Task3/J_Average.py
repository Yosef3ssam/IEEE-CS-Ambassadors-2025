n = int(input())
a = list(map(float,input().split()))
def avrg (n, a):
    total = 0
    for i in a:
        total += i
    return total / n
last = avrg(n, a)
print ('{:.6f}'.format(last))
