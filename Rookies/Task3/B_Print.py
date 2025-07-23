n = int(input())
def print_numbers (n) :
    numbers = []
    for i in range (1, n + 1):
        numbers.append(str(i))
    print (" ".join(numbers))
print_numbers(n)