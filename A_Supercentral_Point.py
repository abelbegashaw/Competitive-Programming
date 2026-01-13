from collections import defaultdict
n = int(input())
points = []
horizontal = defaultdict(lambda : [float("inf"), float("-inf")])
vertical = defaultdict(lambda : [float("inf"), float("-inf")])
for _ in range(n):
    points.append(tuple(map(int, input().split())))
for x, y in points:
    vertical[x][0] = min(vertical[x][0], y)
    vertical[x][1] = max(vertical[x][1], y)
    horizontal[y][0] = min(horizontal[y][0], x)
    horizontal[y][1] = max(horizontal[y][1], x)
result = 0
for x, y in points:
    case_1 = horizontal[y][0] < x < horizontal[y][1]
    case_2 = vertical[x][0] < y < vertical[x][1]
    if case_1 and case_2:
        result += 1
print(result)