t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    array.sort()
    result = float("-inf")
    left = 0
    seen = set([array[0]])
    for right in range(1, n):
        if array[right] - array[right - 1] > 1:
            result = max(result, len(seen))
            left = right
            seen.clear()
        seen.add(array[right])
    result = max(result, len(seen))
    print(result)