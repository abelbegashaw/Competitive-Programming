n = int(input())
result = 0
capacity = 0
for _ in range(n):
    a, b = map(int, input().split())
    capacity += b - a
    result = max(result, capacity)
print(result)