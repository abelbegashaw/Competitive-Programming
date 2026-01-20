n, m = map(int, input().split())
chessboard = [input() for _ in range(n)]
result = [list("BW" * (m//2) + ("B" if m%2 else ""))]
for _ in range(n - 1):
    curr = "B" if result[-1][0] == "W" else "W"
    result.append([curr] + result[-1][:-1])
for i in range(n):
    for j in range(m):
        if chessboard[i][j] == '-':
            result[i][j] = "-"
for row in result:
    print("".join(row))