for i in range(5):
    curr = list(map(int, input().split()))
    if 1 in curr:
        print(abs(2 - i) + abs(2 - curr.index(1)))
        break