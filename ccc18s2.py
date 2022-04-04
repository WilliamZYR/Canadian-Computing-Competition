# https://dmoj.ca/problem/ccc18s2

N = int(input())
data = []
for i in range(N):
    data.append(input().split())

data1 = []
for i in range(1):
    data1 = data
    for j in range(N):
        for k in range(N):
            data[j][k] = int(data1[k][-j-1]) # rotate anticlockwise
    flag = True
    for j in range(N):
        for k in range(N-1):
            if data[j][k] < data[j][k+1] and data[k][j] < data[k+1][j]:
                flag = True
            else:
                flag = False
                continue
        if not flag:
            continue
    if flag:
        print(data)

