s, n = map(int, input().split())
dragons = [list(map(int, input().split())) for _ in range(n)]
dragons.sort()
for strength, bonus in dragons:
    if s <= strength:
        print("NO")
        break
    s += bonus
else:
    print("YES")