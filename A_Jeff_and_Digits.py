n = int(input())
digits = list(map(int, input().split()))
fives, zeros = digits.count(5), digits.count(0)
got = fives // 9 * 9
print(int('5'*got + '0'*zeros)) if zeros else print(-1)