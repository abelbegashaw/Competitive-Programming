n = int(input())
array = list(map(int, input().split()))
single, double = array.count(100), array.count(200)
# 6      46
if single%2 or (double%2 and single < 2):
    print("NO")
else:
    print("YES") 