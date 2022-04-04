# https://dmoj.ca/problem/ccc13s2

"""
W = int(input())
N = int(input())
total = 0
count = 0
weights = []
if N <= 4:
    for i in range(N):
        total += int(input())
        if total <= W:
            count += 1
        else:
            break
    print(count)
elif N > 4:
    for i in range(N):
        weights.append(int(input()))
    four = weights[0] + weights[1] + weights[2] + weights[3]
    if four > W:
        for i in range(4):
            total += weights[i]
            if total <= W:
                count += 1
            else:
                break
        print(count)
    else:
        for i in range(N-3):
            total = 0               #"total" should be renewed each time
            for j in range(4):
                total += weights[i+j]
            if total <= W:
                count += 1
            else:
                break
        print(count+3)
"""

W = int(input())
N = int(input())
total = 0
count = 0
weights = []
for i in range(N):
    weights.append(int(input()))
for i in range(N):
    total += weights[i]
    if i >= 4:
        total -= weights[i - 4]
    if total <= W:
        count += 1
    else:
        break
print(count)
