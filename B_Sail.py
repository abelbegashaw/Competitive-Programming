t, sx, sy, ex, ey = map(int, input().split())
string = input()

hashmap = {"N" : 0, "E" : 0, "W" : 0, "S" : 0,}

for char in string:
    hashmap[char] += 1

delta_x, delta_y = ex - sx, ey - sy
need_x = ["W" if delta_x <= 0 else "E", abs(delta_x)]
need_y = ["S" if delta_y <= 0 else "N", abs(delta_y)]

for index in range(t):
    if string[index] == need_x[0] and need_x[1]:
        need_x[1] -= 1
    
    if string[index] == need_y[0] and need_y[1]:
        need_y[1] -= 1

    if need_x[1] == need_y[1] == 0:
        print(index + 1)
        break
else:
    print(-1)