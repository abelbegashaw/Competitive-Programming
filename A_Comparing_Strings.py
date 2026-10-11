a, b = input(), input()
index_1, index_2 = -1, -1
for i in range(min(len(a),len(b))):
    if a[i] != b[i]:
        if index_1 == -1:
            index_1 = i
        elif index_2 == -1:
            index_2 = i
        else:
            print("NO")
            break
else:
    if not (a[index_1] == b[index_2] and b[index_1] == a[index_2]) or len(a) != len(b):
        print("NO")
    else:
        print("YES")