n = int(input())
scoreCount = {}
for _ in range(n):
    team = input()
    scoreCount[team] = scoreCount.get(team, 0) + 1
answer = result = -1
for team, goal in scoreCount.items():
    if goal > result:
        answer = team
        result = goal
print(answer)