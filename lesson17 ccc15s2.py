# https://dmoj.ca/problem/ccc15s2

J = int(input())
A = int(input())
jersey = {}
for i in range(J):
    jersey[i] = input()
athlete = [[] for i in range(J)]
for i in range(A):
    size, number = map(str, input().split())
    number = int(number)
    athlete[number-1].append(size)
count = 0
for i in range(J):
    if jersey[i] == 'S':
        if 'S' in athlete[i]:
            count += 1
    elif jersey[i] == 'M':
        if 'S' in athlete[i] or 'M' in athlete[i]:
            count += 1
    elif jersey[i] == 'L':
        if 'S' in athlete[i] or 'M' in athlete[i] or 'L' in athlete[i]:
            count += 1
print(count)
