N = int(input())
numbers = list(map(int,input().split()))

min_value = numbers[0]
min_index = 0
for i in range(1, N):
    if numbers[i] < min_value:
        min_value=numbers[i]

        min_index = i
print (min_value, min_index +1 )