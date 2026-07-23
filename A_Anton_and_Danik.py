from typing import Counter


n = int(input())

string = Counter(input())
a, b = string['A'], string['D']
if a > b:
    print("Anton")
elif a < b:
    print("Danik")
else:
    print("Friendship")