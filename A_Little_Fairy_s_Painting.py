t = int(input())
for _ in range(t):
    n = int(input())
    cells = set(map(int, input().split()))
    colors = len(cells)
    while colors not in cells:
        cells.add(colors)
        colors += 1
    print(colors)