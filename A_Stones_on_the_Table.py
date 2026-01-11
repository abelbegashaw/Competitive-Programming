n = int(input())
stones = input()
result = 0
curr = stones[0]
for i in range(1, n):
    if stones[i] == curr:
        result += 1
    else:
        curr = stones[i]
print(result)