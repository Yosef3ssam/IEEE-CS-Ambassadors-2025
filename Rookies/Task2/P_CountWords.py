import re
S = input()
S = re.sub(r'[!.,?]', ' ', S)
word = [word for word in S.split() if word.isalpha()]
print(len(word))