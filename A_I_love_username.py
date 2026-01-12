n = int(input())
points = list(map(int, input().split()))
maxPoint = minPoint = points[0]
result = 0
for i in range(1, n):
    if points[i] > maxPoint:
        maxPoint = points[i]
        result += 1
    
    if points[i] < minPoint:
        minPoint = points[i]
        result += 1
print(result)