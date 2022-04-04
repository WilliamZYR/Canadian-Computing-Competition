# https://dmoj.ca/problem/ccc13s1

'''
n = int(input())
while True:
    n = n + 1
    N = str(n)
    characters = []
    Flag = True
    for i in range(len(N)):
        if N[i] not in characters:
            characters.append(N[i])
        if N[i] in characters:      # elif
            Flag = False
    if Flag:
        print(n)
        break
'''

n = int(input())
while True:
    n = n + 1
    N = str(n)
    characters = []
    for i in range(len(N)):
        if N[i] not in characters:
            characters.append(N[i])
    if len(characters) == len(N):
        print(n)
        break
