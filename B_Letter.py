heading = "".join(input().split())
text = "".join(input().split())

letters = dict()

for char in heading:
    letters[char] = letters.get(char, 0) + 1

for char in text:
    if letters.get(char, 0) == 0:
        print("NO")
        break
    letters[char] -= 1
else:
    print("YES")