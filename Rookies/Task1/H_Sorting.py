N = int(input())
numbers = list(map(int, input().split()))
min_value = 0
min_index = 0

for index, value in enumerate(numbers):
    if value < min_value:
        min_value = value
        min_index = index

print (index)
        