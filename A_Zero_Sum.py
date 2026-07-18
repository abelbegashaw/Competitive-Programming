t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    pos, neg = array.count(1), array.count(-1)
    if pos % 2 == neg % 2 == 0:
        print("YES")
    else:
        print("NO") 