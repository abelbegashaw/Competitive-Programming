n = int(input())
array = list(map(int, input().split()))
min_index, max_index = -1, n
min_val, max_val = float("inf"), float("-inf")
for i in range(n):
    if array[i] > max_val:
        max_val = array[i]
        max_index = i
for i in range(n - 1, -1, -1):
    if array[i] < min_val:
        min_val = array[i]
        min_index = i
print(max_index + n - min_index - 1 - (min_index < max_index))