n = int(input())
a, b = 0, 1
fibs = [a, b]
while b < 10**9:
    a, b = b, a + b
    fibs.append(b)
flag = False
for i in range((len(fibs))):
    for j in range(len(fibs)):
        for k in range(len(fibs)):
            if fibs[i] + fibs[j] + fibs[k] == n:
                print(fibs[i], fibs[j], fibs[k])
                flag = True
                break
        if flag:
            break
    if flag:
        break
else:
    print("I'm too stupid to solve this problem")
