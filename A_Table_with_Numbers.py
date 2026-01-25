from collections import Counter
t = int(input())
"""
5 2 2

_ _ _
_ _ _
_ _ _
_ _ _
_ _ _
_ _ _

10: 1
4: 2
1: 1
3: 1
6: 1
"""
for _ in range(t):
    n, h, l = map(int, input().split())
    array = list(map(int, input().split()))
    counts = Counter(array)
    result = 0
    for j in range(l + 1, 1, -1):
        for i in range(1, h + 1):
            while counts[i] > 0 and counts[j] > 0:
                if i == j and counts[i]  < 2:
                    break
                counts[i] -= 1
                counts[j] -= 1
                result += 1
    print(result)