n, m = map(int, input().split())
planes = list(map(int, input().split()))

# Getting the maximum profit
maxPlanes = planes[:]
maxGain = 0
passengers = n
while passengers:
    max_val = max(maxPlanes)
    max_index = maxPlanes.index(max_val)
    maxGain += max_val
    maxPlanes[max_index] -= 1
    passengers -= 1

# Getting the minimum profit
minPlanes = planes[:]
minGain = 0
passengers = n
while passengers:
    min_val = min(minPlanes)
    min_index = minPlanes.index(min_val)
    minGain += min_val
    minPlanes[min_index] -= 1
    if minPlanes[min_index] == 0:
        minPlanes[min_index] = float("inf")
    passengers -= 1
    
print(maxGain, minGain)