s = input()
fours = 0
for i in range(len(s) - 1, -1, -1):
    if s[i] == '1':
        fours = 0
    fours += s[i] == '4'
    condition_1 = s[i] != '1' and s[i] != '4'
    condition_2 = fours > 2
    
    if condition_1 or condition_2:
        print("NO")
        break
else:
    print("YES") if fours == 0 else print("NO")