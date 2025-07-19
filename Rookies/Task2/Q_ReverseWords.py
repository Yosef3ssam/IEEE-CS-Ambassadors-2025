S = input()
words = S.split()
reversed = [word[::-1] for word in words]
output = ' '.join(reversed)
print(output)