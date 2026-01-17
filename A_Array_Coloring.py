t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    for i in range(n - 1):
        if array[i] % 2 == array[i + 1] % 2:
            print("NO")
            break
    else:
        print("YES")