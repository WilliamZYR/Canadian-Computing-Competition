N = int(input)
for i in range(N):
    r = int(input())
    c = int(input())
    matrix = []
    for j in range(r):



for i in range(N-1):

    NumberOfColumns = 1
    NumberOfRows = 1
    l = [[0 for j in range(NumberOfColumns)] for i in range(NumberOfRows)]

    N = int(input())
    for i in range(N):
        r, c = map(int, input().split())
        matrix = []

        for rowNum in range(r):
            temp = list(map(int, input().split()))
            matrix.append(temp)
