actions = [input().split() for _ in range(3)]
result = [['1' for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        if int(actions[i][j]) % 2:
            result[i][j] = '1' if result[i][j] == '0' else '0'
            if i != 0:
                result[i - 1][j] = '1' if result[i - 1][j] == '0' else '0'
            
            if i != 2:
                result[i + 1][j] = '1' if result[i + 1][j] == '0' else '0'
            
            if j != 0:
                result[i][j - 1] = '1' if result[i][j - 1] == '0' else '0'
            
            if j != 2:
                result[i][j + 1] = '1' if result[i][j + 1] == '0' else '0'
            
for row in result:
    print("".join(row))