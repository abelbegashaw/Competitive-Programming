n = int(input())
for _ in range(n):
    word = input()
    print(word[0] + f"{len(word) - 2}" + word[-1]) if len(word) > 10 else print(word)