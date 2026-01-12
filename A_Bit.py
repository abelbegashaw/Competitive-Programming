n = int(input())
result = 0
for _ in range(n):
    line = input()
    result += '+' in line
    result -= '-' in line
print(result)