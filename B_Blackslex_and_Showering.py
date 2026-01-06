t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    totalTime = 0
    for i in range(1, n):
        totalTime += abs(array[i] - array[i - 1])
    result = totalTime
    for i in range(1, n - 1):
        left = abs(array[i] - array[i - 1])
        right = abs(array[i] - array[i + 1])
        diff = abs(array[i - 1] - array[i + 1])
        result = min(result, totalTime - left - right + diff)
    print(
        min(
            result,
            totalTime - abs(array[1] - array[0]),            
            totalTime - abs(array[-1] - array[-2]),            
        )
    )