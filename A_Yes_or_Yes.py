t = int(input())
for _ in range(t):
    string = input()
    print(["NO", "YES"][string.count('Y') <= 1])