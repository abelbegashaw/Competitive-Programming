memo = {}
def dfs(n, k):
    if n == k:
        return 0
    if n < k:
        return float("inf")
    state = (n, k)
    if state not in memo:
        if n%2:
            memo[state] = 1 + min(dfs(n//2, k), dfs(n - n//2, k))
        else:
            memo[state] = 1 + dfs(n//2, k)
    return memo[state]

n = int(input())
for _ in range(n):
    n, k = map(int, input().split())
    ans = dfs(n, k)
    print(-1) if ans == float("inf") else print(ans)