N = int(input())
numbers = list(map(int,input().split()))
X = int(input())
found = False
for index, number in enumerate(numbers):
    if number == X :
        print(index)
        found = True
        break
if not found:
    print(-1)