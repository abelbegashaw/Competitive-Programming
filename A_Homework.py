t = int(input())
for _ in range(t):
    n, a = int(input()), input()
    m, b, c = int(input()), input(), input()
    prefix, suffix = '', ''
    for i in range(m):
        if c[i] == 'V':
            prefix = b[i] + prefix
        else:
            suffix += b[i]
    print(prefix + a + suffix)