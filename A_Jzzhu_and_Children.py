n, m = map(int, input().split())
array = list(map(int, input().split()))
maxVal = lastIndex = 0
for i in range(n):
    rounds = array[i] // m + (array[i] % m != 0)
    if rounds >= maxVal:
        maxVal = rounds
        lastIndex = i + 1
print(lastIndex)