n = int(input())
pages = list(map(int, input().split()))
rate = sum(pages)
n -= n//rate * rate
if n == 0:
    n += rate
for i in range(7):
    if n - pages[i] <= 0:
        print(i + 1)
        break
    n -= pages[i]