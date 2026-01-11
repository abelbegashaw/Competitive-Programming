x, y = input(), input()
a = int(x, 2)
b = int(y, 2)
result = bin(a ^ b)[2:]
print('0'*(len(x) - len(result)) + result)