f1, f2, f3 = map(int, input().split())
a = (f1 * f3 / f2) ** 0.5
b = f2 * a / f3
c = f3 / a
print(4 * int(a + b + c))