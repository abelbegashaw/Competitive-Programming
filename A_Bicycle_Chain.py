n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
ratios = {}
for i in range(n):
    for j in range(m):
        if b[j] % a[i] == 0:
            ratios[b[j] // a[i]] = ratios.get(b[j] // a[i], 0) + 1
currMAx = 0
for ratio, count in ratios.items():
    if ratio > currMAx:
        currMAx = ratio
print(ratios.get(currMAx, 0))