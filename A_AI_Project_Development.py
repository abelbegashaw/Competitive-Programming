t = int(input())

for _ in range(t):
    n, x, y, z = map(int, input().split())
    time_1 = n // (x + y) + (n % (x + y) != 0)
    time_2 = z + (n - x * z) // (x + 10 * y) + ((n - x * z) % (x + 10 * y) != 0)
    print(min(time_1, time_2))