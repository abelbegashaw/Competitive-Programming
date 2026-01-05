t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    result = 0
    k1 = k2 = 0
    for j in range(n):
        head = legs = True
        for i in range(n):
            if b[(j + i) % n] <= a[i]:
                head = False
        
        for k in range(n):
            if b[(j + k) % n] >= c[k]:
                legs = False
        
        k1, k2 = k1 + head, k2 +  legs
        
    print(k1 * k2 * n)