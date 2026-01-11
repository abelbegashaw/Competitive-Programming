actions = [input().split() for _ in range(3)]
result = [['1' for _ in range(3)] for _ in range(3)]

def inbound(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def toggle(x, y):
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    result[x][y] = '1' if result[x][y] == '0' else '0'
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if inbound(new_x, new_y):
            result[new_x][new_y] = '1' if result[new_x][new_y] == '0' else '0'

for i in range(3):
    for j in range(3):
        if int(actions[i][j]) % 2:
            toggle(i, j)

for row in result:
    print("".join(row))