A, B = map(int, input().split())
S = input()


if len(S) != A + B + 1:
    print("No")

elif S[A] != '-':
    print("No")

elif not (S[:A] + S[A+1:]).isdigit():
    print("No")
else:
    print("Yes")
