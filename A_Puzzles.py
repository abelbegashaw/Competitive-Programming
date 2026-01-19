n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
result = array[-1]
for i in range(m - n + 1):
    result = min(result, array[i + n - 1] - array[i])
print(result)