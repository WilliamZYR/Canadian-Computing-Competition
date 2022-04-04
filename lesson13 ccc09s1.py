# https://dmoj.ca/problem/ccc09s1
"""
a = int(input())
b = int(input())
count = 0
for i in range(a, b+1, +1):
    square = False
    cube = False
    for j in range(0, i+1, +1):
        if i == pow(i, 2):
            square = True
        if i == pow(i, 3):
            cube = True
        if square is True and cube is True:
            count += 1
            break
print(count)
"""

"""
a = int(input())
b = int(input())
count = 0
for i in range(a, b+1, +1):
    for j in range(0, i+1, +1):
        if i == pow(j, 6):
            count += 1
            break
print(count)
"""

a = int(input())
b = int(input())
countA = 0
countB = 0
for i in range(1, 22, +1):
    if a > pow(i, 6):
        countA += 1
for i in range(1, 22, +1):
    if b >= pow(i, 6):
        countB += 1
print(countB - countA)
