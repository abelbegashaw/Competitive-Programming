t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    answer_1, answer_2 = 0, 0
    cakes, turn = [a, b], 0
    size = 1
    while size <= cakes[turn]:
        cakes[turn] -= size
        turn = 1 - turn
        answer_1 += 1
        size *= 2
    cakes, turn = [a, b], 1
    size = 1
    while size <= cakes[turn]:
        cakes[turn] -= size
        turn = 1 - turn
        answer_2 += 1 
        size *= 2
    print(max(answer_1, answer_2))