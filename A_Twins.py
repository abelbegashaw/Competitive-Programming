n = int(input())
coins = list(map(int, input().split()))
total = sum(coins)
coins.sort(reverse=True)
runningSum = 0
for i in range(n):
    runningSum += coins[i]
    if runningSum > total - runningSum:
        print(i + 1)
        break