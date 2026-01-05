import math
t = int(input())
for _ in range(t):
    n = int(input())
    d = 10
    result = []
    while d + 1 <= n:
        if n % (d + 1) == 0:
            result.append(n // (d + 1))
        d *= 10
    result.reverse()
    print(len(result))
    if result:
        print(*result)