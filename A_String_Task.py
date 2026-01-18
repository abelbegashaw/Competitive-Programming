vowels = "aeiouy"
string = input().lower()
result = []
for char in string:
    if char not in vowels:
        result.append(f".{char}")
print("".join(result))