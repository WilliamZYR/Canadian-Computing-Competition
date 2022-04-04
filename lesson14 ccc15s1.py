# https://dmoj.ca/problem/ccc15s1

'''
N = int(input())
integers = [0]
for i in range(N):
    integer = int(input())
    if integer != 0:
        integers.append(integer)
    else:
        del integers[len(integers)-1]
count = 0
for i in range(len(integers)):
    count += integers[i]
print(count)
'''

N = int(input())
integers = []
for i in range(N):
    integer = int(input())
    if integer != 0:
        integers.append(integer)
    else:
        integers.pop()
count = 0
for i in range(len(integers)):
    count += integers[i]
print(count)