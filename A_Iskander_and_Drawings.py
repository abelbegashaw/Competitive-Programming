t = int(input())

for _ in range(t):
    n = int(input())
    s = input().split("*")
    result = 0
    for chunk in s:
        result = max(result, (len(chunk) + 1) // 2)
    print(result)    