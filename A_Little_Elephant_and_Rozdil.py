n = int(input())
towns = list(map(int, input().split()))
minIndex = towns.index(min(towns))
print("Still Rozdil") if towns.count(towns[minIndex]) > 1 else print(minIndex + 1)