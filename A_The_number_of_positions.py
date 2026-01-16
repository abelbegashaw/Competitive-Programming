n, a, b = map(int, input().split())
if a < n - b:
    print(b + 1)
else:
    print(n - a)