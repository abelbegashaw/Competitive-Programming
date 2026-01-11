word = input()
lowerCase = upperCase = 0
for char in word:
    lowerCase += char.islower()
    upperCase += char.isupper()
if lowerCase >= upperCase:
    word = word.lower()
else:
    word = word.upper()
print(word)