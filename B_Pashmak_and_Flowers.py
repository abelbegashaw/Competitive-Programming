n = int(input())
flowers = list(map(int, input().split()))
max_val, min_val = max(flowers),  min(flowers)
if max_val == min_val:
    print(0, flowers.count(max_val) * (flowers.count(min_val) - 1) // 2)
else:
    print(max_val - min_val, flowers.count(max_val) * flowers.count(min_val))