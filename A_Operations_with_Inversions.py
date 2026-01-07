t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    result = 0
    for i in range(n):
        for j in range(i + 1, n):
            if array[i] > array[j]:
                print(array[i], array[j])
                array[j] = n
                result += 1
    print(result)