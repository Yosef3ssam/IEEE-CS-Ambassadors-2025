N = int(input())
A = list(map(int, input().split()))

min_value = min(A)
count = A.count(min_value)

if count % 2 != 0:
    print('Lucky')
else:
     print('Unlucky')