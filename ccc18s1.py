# https://dmoj.ca/problem/ccc18s1

N = int(input())
V = []
for i in range(N):
    V.append(int(input()))
V.sort()
distance = 1000000000
for i in range(N-2):
    if (V[i+2] - V[i])/2 <= distance:
        distance = (V[i+2] - V[i])/2
print(float(distance))
