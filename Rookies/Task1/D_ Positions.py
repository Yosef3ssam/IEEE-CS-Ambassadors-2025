N = int(input())
numbers = list (map(int,input().split()))
for index, number in enumerate(numbers):
    if number <= 10:
        print(f"A[{index}] = {number}")