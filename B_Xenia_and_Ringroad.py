n, m = map(int, input().split())
tasks = list(map(int, input().split()))
curr = 1
result = 0
for task in tasks:
    if curr < task:
        result += task - curr
    elif curr > task:
        result += task + n - curr
    curr = task
print(result)