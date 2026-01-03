t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    result = index = 0
    while index < n:
        if s[index] == '0':
            result += 1
        else:
            curr_one = index
            for i in range(index, min(index + k + 1, n)):
                if s[i] == '1':
                    curr_one = i
            index = curr_one + k
        index += 1
    print(result)