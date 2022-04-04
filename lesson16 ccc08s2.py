# https://dmoj.ca/problem/ccc08s2

'''
while True:
    r = int(input())
    if r == 0:
        break
    count = 4 * r + 1
    for i in range(1, r+1, +1):
        for j in range(1, r+1, +1):
            if i * i + j * j <= r * r:
                count += 4
    print(count)
'''

import math
while True:
    r = int(input())
    if r == 0:
        break
    count = 4 * r + 1

    for i in range(1, r + 1):
        count += int(math.sqrt(r * r - i * i)) * 4

    print(count)
