n = int(input())
result = 0
left = right = 0
for _ in range(n):
    cupBoard = list(map(int, input().split()))
    left, right = left + cupBoard[0], right + cupBoard[1]
print(min(left, n - left) + min(right, n - right))