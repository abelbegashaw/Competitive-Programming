from collections import Counter
names = input()
names += input()
pile = Counter(input())
letterCount = {}
for char in names:
    letterCount[char] = letterCount.get(char, 0) + 1
print("YES") if letterCount == pile else print("NO")