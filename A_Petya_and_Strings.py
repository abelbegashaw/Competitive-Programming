string_one, string_two = input().lower(), input().lower()
if string_one < string_two:
    print(-1)
elif string_one > string_two:
    print(1)
else:
    print(0)