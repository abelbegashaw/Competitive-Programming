from collections import defaultdict
n = int(input())
array = list(map(int, input().split()))
m = input()
queries = list(map(int, input().split()))

chunks = defaultdict(list)
for i in range(n):
    chunks[array[i]].append(i)

vasya = petya = 0
for query in queries:
    vasya += chunks[query][0] + 1
    petya += n - chunks[query][-1]
print(vasya, petya)