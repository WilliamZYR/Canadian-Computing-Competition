# https://dmoj.ca/problem/ccc01s2

x = int(input())
y = int(input())
spiral = [[x]]
for i in range(5):
    spiral.append([])
    for j in range(2*i + 2):
        x += 1
        spiral[-1].append(x)
        if x == y or x == 99:
            break
    if x == y or x == 99:
        break
    for j in range(2*i + 1):
        x += 1
        spiral[-j-2].append(x)
        if x == y or x == 99:
            break
    if x == y or x == 99:
        break
    new1 = [[]]
    new2 = [' ']
    spiral = new1 + spiral
    for j in range(2*i + 2):
        spiral[0].append(' ')
    for j in range(2*i + 2):
        x += 1
        spiral[0][-1-j] = x
        if x == y or x == 99:
            break
    if x == y or x == 99:
        break
    for j in range(2*i + 3):
        spiral[j] = new2 + spiral[j]
    for j in range(2*i + 3):
        x += 1
        spiral[j][0] = x
        if x == y or x == 99:
            break
    if x == y or x == 99:
        break
for i in range(len(spiral)):
    for j in range(len(spiral[i])):
        if spiral[i][j] == ' ':
            print(" ", end=" ")
        else:
            print(spiral[i][j], end=" ")
    print()
