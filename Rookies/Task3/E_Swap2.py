def swap(numbers):
    numbers = list(numbers)
    for num in numbers[::-1]:
        print(num, end=" ")

numbers= map(int,input().split())
swap(numbers)