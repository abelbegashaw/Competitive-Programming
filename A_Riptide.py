t = int(input())
for _ in range(t):
    tokens = list(map(int, input().split()))
    tokens.sort()
    print(min(tokens[-1] - tokens[-2], tokens[-2] - tokens[-3]))