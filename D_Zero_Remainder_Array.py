t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    array = list(map(int, input().split()))
    remainder = {}
    for i in range(n):
        needed = (k - array[i] % k) % k
        remainder[needed] = remainder.get(needed, 0) + 1 
    max_val, max_freq  = 0, 0
    for val, freq in remainder.items():
        if val != 0:
            if freq >= max_freq:
                if freq > max_freq:
                    max_val = val
                else:
                    max_val = max(max_val, val)
                max_freq = freq
    print(max(0, (max_freq - 1) * k + max_val + 1))