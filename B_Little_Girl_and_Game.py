from collections import Counter
s = input()

counts = Counter(s)
odds = 0
for char, num in counts.items():
    odds += num % 2 == 1

if odds % 2 or odds == 0:
    print("First")
else:
    print("Second")