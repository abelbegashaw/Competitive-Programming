t = int(input())
for _ in range(t):
    n, m, h = map(int, input().split())
    a = list(map(int, input().split()))
    result = a[:]
    globalFlip = 0
    localFlip = [0 for _ in range(n)]
    for _ in range(m):
        idx, val = map(int, input().split())
        if localFlip[idx - 1] == globalFlip:
            result[idx - 1] += val

        elif localFlip[idx - 1] < globalFlip:
            localFlip[idx - 1] = globalFlip
            result[idx - 1] = a[idx - 1] + val
            
        if result[idx - 1] > h:
            result[idx - 1] = a[idx - 1]
            globalFlip += 1
    for i in range(n):
        if localFlip[i] != globalFlip:
            result[i] = a[i]
    print(*result)