k = int(input())
growth = list(map(int, input().split()))
growth.sort()
result = height = 0
index = len(growth) - 1
while index > -1 and k > 0:
    k -= growth[index]
    index -= 1
    result += 1
print(result) if k <= 0 else print(-1)