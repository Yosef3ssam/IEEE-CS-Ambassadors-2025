s = input()
converted = ""

for char in s:
    if char == ',':
        converted += ' '
    elif char.islower():
        converted += char.upper()
    elif char.isupper():
        converted += char.lower()

print(converted)
