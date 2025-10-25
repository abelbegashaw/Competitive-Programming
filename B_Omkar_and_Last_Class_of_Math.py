t = int(input())

for _ in range(t):
    n = int(input())
    largest = 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            largest = d
        d += 1
    print(largest, n - largest)
    