s = input()
t = "hello"
index = 0
for i in range(len(s)):
    if s[i] == t[index]:
        index += 1
        if index == 5:
            print("YES")
            break
else:
    print("NO")