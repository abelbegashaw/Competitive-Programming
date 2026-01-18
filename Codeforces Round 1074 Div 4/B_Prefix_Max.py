t = int(input())
for _ in range(t):
    n = int(input())
    maximum = max(list(map(int, input().split())))
    print(maximum * n)