year = int(input())
while True:
    year += 1
    if len(set(f"{year}")) == 4:
        print(year)
        break