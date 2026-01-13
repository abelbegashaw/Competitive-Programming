n = int(input())
array = list(map(int, input().split()))
diff = index = float("inf")
for i in range(n):
    if abs(array[i] - array[(i + 1)%n]) < diff:
        diff = abs(array[i] - array[(i + 1)%n])
        index = i
print(index + 1, (index + 1) % n + 1)