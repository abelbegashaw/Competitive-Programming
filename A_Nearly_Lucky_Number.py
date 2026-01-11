number = input()
luckyDigits = number.count('4') + number.count('7')
print("YES") if luckyDigits == 4 or luckyDigits == 7 else print("NO")