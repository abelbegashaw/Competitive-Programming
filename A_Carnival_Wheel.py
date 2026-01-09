t = int(input())
for _ in range(t):
    l, a, b = map(int, input().split())
    k = (l - a) // b
    print(a + k * b) if (l - a) % b else print(l - b)
    """
    0 1 2 3 4

    (3 + 2K) % 5 = 4

    2K % 5 = 1
    
    2K = 1
    K = 1/2
    """