# https://dmoj.ca/problem/ccc20s2

import math
M = int(input())
N = int(input())
rooms = []
for i in range(M):
    rooms.append(input().split())
for i in range(M):
    for j in range(N):
        rooms[i][j] = int(rooms[i][j])
past = [[0, 0]]
a = -1
while True:
    a += 1
    room = rooms[past[a][0]][past[a][1]]

    if M * N == room:
        print("yes")
        break

    max = int(math.sqrt(room))
    for i in range(1, max+1):
        if room%i == 0:
            if [i-1, int(room/i-1)] not in past and i-1 <= M-1 and int(room/i-1) <= N-1:
                past.append([i-1, int(room/i-1)])
            if [int(room/i-1), i-1] not in past and i-1 <= N-1 and int(room/i-1) <= M-1:
                past.append([int(room/i-1), i-1])
    if a+2 > len(past):
        print("no")
        break
