n = int(input())
x = y = z = 0
for _ in range(n):
    forces = list(map(int, input().split()))
    x += forces[0]
    y += forces[1]
    z += forces[2]
print("YES") if x == y == z == 0 else print("NO")