t = int(input())

for _ in range(t):

    n = int(input())
    array = list(map(int, input().split()))
    array.sort()

    """
    1 1 2 3 3 4 5 5 5 6 9

    1 2 3 4 5 6 9
    2 1 2 1 3 1 1

    2 + 2 + 6 + 4 + 15 + 6 + 9 


    2 

    """
    print(*array)