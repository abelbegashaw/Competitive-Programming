n, k = map(int, input().split())
array = list(map(int, input().split()))

for i in range(k, n):
    if array[k - 1] != array[i]:
        print(-1)
        break
else:
    index = k - 1
    while k > 0 and array[index] == array[k - 1]:
        k -= 1
    print(k)
