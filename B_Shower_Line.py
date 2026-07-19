patterns = []

def backtrack(curr, options):

    if not options:
        patterns.append(curr.copy())
        return
    
    for i in range(len(options)):
        curr.append(options[i])
        options.pop(i)
        backtrack(curr, options)
        num = curr.pop()
        options.insert(i, num)


backtrack([], [1, 2, 3, 4, 5])

matrix = [list(map(int, input().split())) for _ in range(5)]

result = 0
for pattern in patterns:
    answer = 0
    for i in range(1, len(pattern)):
        x, y = pattern[i] - 1, pattern[i - 1] - 1
        answer += matrix[x][y] + matrix[y][x]
        if i > 2:
            answer += matrix[x][y] + matrix[y][x]
    result = max(result, answer)
print(result)