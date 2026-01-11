n, t = map(int, input().split())
queue = list(input())
while t:
    i = 0
    while i < n - 1:
        if queue[i] == 'B' and queue[i + 1] == 'G':
            queue[i], queue[i + 1] = queue[i + 1], queue[i]
            i += 1
        i += 1
    t -= 1
print("".join(queue))