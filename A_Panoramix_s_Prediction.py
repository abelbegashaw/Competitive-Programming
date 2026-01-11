def isPrime(number):
    d = 2
    while d * d <= number:
        if number % d == 0:
            return False
        d += 1
    return True

n, m = map(int, input().split())
for num in range(n + 1, m):
    if isPrime(num):
        print("NO")
        break
else:
    print("YES") if isPrime(m) else print("NO")