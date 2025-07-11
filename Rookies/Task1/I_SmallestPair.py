T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split())) 

    min_result = float('inf')

    for i in range(N):
        for j in range(i + 1, N):
            result = A[i] + A[j] + (j - i)
            if result < min_result:
                min_result = result

    print(min_result)
