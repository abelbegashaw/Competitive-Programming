def nPrimes(number):
    result = []
    curr = 2
    while number:
        d = 2
        flag = True
        while d * d <= curr:
            if curr % d == 0:
                flag = False
                break
            d += 1
        if flag:
            result.append(curr)
            number -= 1
        curr += 1
    return result

t = int(input())
primes = nPrimes(55)
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    result = 100
    for num in array:
        for prime in primes:
            if num % prime:
                result = min(result, prime)
                break
    print(result)


def nPrimes(number):
    result = []
    curr = 2
    while number:
        d = 2
        flag = True
        while d * d <= curr:
            if curr % d == 0:
                flag = False
                break
        if flag:
            result.append(curr)
            number -= 1
        curr += 1
    return result
