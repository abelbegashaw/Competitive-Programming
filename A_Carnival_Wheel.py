t = int(input())
for _ in range(t):
    l, a, b = map(int, input().split())
    k = (l - a) // b
    print(a + k * b) if (l - a) % b else print(l - b)