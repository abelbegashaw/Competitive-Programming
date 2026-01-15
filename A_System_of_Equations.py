n, m = list(map(int, input().split()))
result = 0
for a in range(m + 1):
    b = (m - a) ** 0.5
    if b != int(b):
        continue
    result += a*a + b == n
print(result)