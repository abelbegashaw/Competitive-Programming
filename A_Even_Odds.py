n, k = map(int, input().split())
odds, evens = n//2 + (n%2 != 0), n//2
print(2*(k - odds)) if k > odds else print(2*k - 1)