from collections import defaultdict

n = int(input())
array = list(map(int, input().split()))

counts = defaultdict(int)
for num in array:
    counts[num] = counts.get(num, 0) + 1

if not (counts[1] == counts[2] + counts[3] == counts[4] + counts[6]) or 5 in counts or 7 in counts:
    print(-1)
else:
    flag = False
    answers = []
    while counts[1] > 0:
        if counts[2] > 0:
            if counts[4] > 0:
                answers.append([1,2,4])
                counts[1], counts[2], counts[4] = counts[1] - 1, counts[2] - 1, counts[4] - 1
            elif counts[6] > 0:
                answers.append([1, 2, 6])
                counts[1], counts[2], counts[6] = counts[1] - 1, counts[2] - 1, counts[6] - 1
            else:
                flag = not flag
                break
        elif counts[3] > 0 and counts[6] > 0:
            answers.append([1, 3, 6])
            counts[1], counts[3], counts[6] = counts[1] - 1, counts[3] - 1, counts[6] - 1
        else:
            flag = not flag
            break
    if flag:
        print(-1)
    else:
        for answer in answers:
            print(*answer)
