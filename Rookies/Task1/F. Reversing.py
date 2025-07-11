N = int(input())
numbers = list(map(int,input().split()))
for number in range (N -1, -1,-1) :
    print(numbers[number], end=' ')
