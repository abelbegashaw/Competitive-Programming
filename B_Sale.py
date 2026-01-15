n, m = map(int, input().split())
tvs = list(map(int, input().split()))
tvs.sort()
result = 0
for i in range(m):
    result += -tvs[i] if tvs[i] < 0 else 0
print(result)