# https://dmoj.ca/problem/ccc16s2

Q = int(input())
N = int(input())
D = input().split()
P = input().split()
for i in range(N):
    D[i] = int(D[i])
    P[i] = int(P[i])
D.sort()
P.sort()
speed = [[] for i in range(N)]
total = 0
if Q == 1:
    for i in range(N):
        speed[i].append(D[i])
        speed[i].append(P[i])
        speed[i].sort()
        total += speed[i][1]
if Q == 2:
    for i in range(N):
        speed[i].append(D[i])
        speed[i].append(P[-i-1])
        speed[i].sort()
        total += speed[i][1]
print(total)
