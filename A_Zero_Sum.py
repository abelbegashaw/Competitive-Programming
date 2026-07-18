t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    delta = abs(array.count(1) - array.count(-1))
    if n % 2 or delta % 2 or (delta // 2) % 2:
        print("NO")
    else:
        print("YES") 