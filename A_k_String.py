from collections import Counter
k = int(input())
string = input()
if len(string) % k:
    print(-1)
else:
    result = []
    characters = Counter(string)
    for letter in characters:
        if characters[letter] % k:
            print(-1)
            break
        result.append(letter * (characters[letter] // k))
    else:
        print("".join(result) * k)