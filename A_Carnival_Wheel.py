t = int(input())
for _ in range(t):
    l, a, b = map(int, input().split())
    wheel = [False for _ in range(l)]
    result = a
    while not wheel[a]:
        result = max(result, a)
        wheel[a] = True
        a = (a + b) % l
    print(result)