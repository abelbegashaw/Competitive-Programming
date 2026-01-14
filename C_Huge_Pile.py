t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    steps = 0
    if n == k:
        print(steps)
    else:
        notFound = True
        while n > k:
            steps += 1
            if n // 2 == k or n - n//2 == k:
                print(steps)
                notFound = False
                break
            n //= 2
        if notFound:
            print(-1)