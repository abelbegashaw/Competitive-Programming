from collections import defaultdict
n = int(input())
array = list(map(int, input().split()))
counts = defaultdict(list)
for i in range(n):
    counts[array[i]].append(i)
result = []
for number, indices in counts.items():
    if len(indices) == 1:
        result.append((number, 0))
    else:
        diff = indices[1] - indices[0]
        
        for i in range(1, len(indices)):
            if indices[i] - indices[i - 1] != diff:
                break
        else:
            result.append((number, diff))
result.sort()
print(len(result))
for x, y in result:
    print(x, y)