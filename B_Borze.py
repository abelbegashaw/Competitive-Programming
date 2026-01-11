code = input()
result = []
index = 0
while index < len(code):
    if code[index] == '.':
        result.append('0')
    else:
        if code[index + 1] == '.':
            result.append('1')
        else:
            result.append('2')
        index += 1
    index += 1
print("".join(result))