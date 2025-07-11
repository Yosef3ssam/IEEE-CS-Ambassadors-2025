N = int(input())
numbers = list(map(int, input().split()))



reversed_numbers = []
for i in range(N - 1, -1, -1):
    reversed_numbers.append(numbers[i])

if numbers == reversed_numbers:
    print("YES")
else:
    print("NO")
