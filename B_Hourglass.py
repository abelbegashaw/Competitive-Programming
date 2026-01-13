n = int(input())
for _ in range(n):
    s, k, m = map(int, input().split())
    lastFlip = m // k * k
    diff = m - lastFlip
    if (m//k) % 2:
        print(max(0, min(s, k) - diff))
    else:
        print(max(0, s - diff))