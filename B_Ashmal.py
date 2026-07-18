from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    a = input().split()
    result = ""
    for string in a:
        if string + result <= result + string:
            result = string + result
        else:
            result = result + string
    print(result)