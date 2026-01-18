n = int(input())
image = [[" " for _ in range(2*n + 1)] for _ in range(2*n + 1)]
image[n] = [i for i in range(n + 1)] + [i for i in range(n - 1, -1, -1)]
for i in range(2*n + 1):
    for dy in range(image[n][i] - 1, -1, -1):
        image[n - dy][i] = image[n][i] - dy
        image[n + dy][i] = image[n][i] - dy
for row in image:
    row = [str(item) for item in row]
    print(" ".join(row).rstrip())