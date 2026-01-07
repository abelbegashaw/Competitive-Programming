scores = list(map(int, input().split()))
scores.sort()
if max(scores) - min(scores) >= 10:
    print("check again")
else:
    print(f"final {scores[1]}")