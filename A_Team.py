n = int(input())
result = 0
for _ in range(n):
    result += sum(map(int, input().split())) > 1
print(result)