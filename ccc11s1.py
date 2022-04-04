# https://dmoj.ca/problem/ccc11s1

n = int(input())
T = 0
S = 0
for i in range(n):
    line = input()
    for char in line:
        if char == 't' or char == 'T':
            T += 1
        if char == 's' or char == 'S':
            S += 1
if T > S:
    print("English")
else:
    print("French")
