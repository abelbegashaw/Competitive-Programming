t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    result = index = 0
    last_one = float("-inf")
    while index < n:
        if s[index] == '0':
            result += index - k > last_one
        else:
            last_one = index
        index += 1
    print(result)