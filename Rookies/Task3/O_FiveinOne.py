n = int(input())
a = list(map(int,input().split()))
def minmax (a):
    max_val = a[0]
    min_val = a[0]
    for i in range(len(a)):
        if max_val < a[i] :
            max_val = a[i]
        if min_val > a[i] :
            min_val = a[i]
    return max_val , min_val
max_num, min_num = minmax(a)
print('The maximum number : ' + str(max_num))
print('The minimum number : ' + str(min_num))

# got the the max and the min :D


n = int(n)
def prime (a):
    prime_num = []
    if a < 2 :
        return False
    for i in range(2 , int(a**0.5 + 1)) :
        if a % i == 0:
            return False
    return True

def count_prime(a):
    primes = []
    
    for i in a :
        if prime(i):
            primes.append(i)
    print("The number of prime numbers : " + str(len(primes)))

count_prime(a)


# got the prime numbers :D

def palindrome (a):
    return str(a) == str(a)[::-1]
        
def palindrome_counter(a):
    palindrome_num =[]
    for i in a:
        if palindrome(i):
            palindrome_num.append (i)
    print('The number of palindrome numbers : ' + str(len(palindrome_num)))

palindrome_counter(a)

# done with the palindrome


def max_devisor_number (a):
    max_divisors = 0
    number_with_max = 0
    
    for num in a:
        divisor_count = 0
        for i in range (1 ,num + 1):
            if num % i == 0:
                divisor_count += 1

        if divisor_count > max_divisors :
            max_divisors = divisor_count
            number_with_max = num

        elif divisor_count == max_divisors:
            number_with_max = max(number_with_max, num)

    return number_with_max

print('The number that has the maximum number of divisors : ' + str((max_devisor_number(a))))