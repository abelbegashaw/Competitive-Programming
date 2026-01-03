t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    year_1, year_2 = "2026", "2025"
    swap_1, swap_2 = 4, 1 if year_2 in s else 0
    for i in range(n - 3):
        count = 0
        for c in range(4):
            count += year_1[c] != s[i + c]
        swap_1 = min(swap_1, count)
    
    print(min(swap_1, swap_2))