k, n, w = map(int, input().split())
print(max(0, (k + k*w)*w//2 - n))