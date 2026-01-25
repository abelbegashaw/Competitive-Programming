from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    a = input().split()
    queue = deque([])
    for string in a:
        if not queue:
            queue.append(string)
        elif string + queue[0] <= queue[0] + string:
            queue.appendleft(string)
        else:
            queue.append(string)
    print("".join(queue))