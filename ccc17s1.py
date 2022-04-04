# https://dmoj.ca/problem/ccc17s1

N = int(input())
Swifts = []
Semaphores = []
Swifts.append(input().split())
Semaphores.append(input().split())    # why 2d list???
day = 0
sum1 = 0
sum2 = 0
for i in range(N):
    sum1 += int(Swifts[0][i])
    sum2 += int(Semaphores[0][i])
    if sum1 == sum2:
        day = i + 1
print(day)
