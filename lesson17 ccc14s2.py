# https://dmoj.ca/problem/ccc14s2
'''
N = int(input())
name1 = input().split()
name2 = input().split()
partners = {}
for i in range(N):
    partners[name1[i]] = name2[i]
Flag = True
for i in range(N):
    if name1[i] == partners[partners[name1[i]]]:    # REMOVE THIS IF STATEMENT!!!
        Flag = True
    elif name1[i] != partners[partners[name1[i]]] or name1[i] == partners[name1[i]]:
        Flag = False
        break
if Flag:
    print("good")
else:
    print("bad")
'''

N = int(input())
name1 = input().split()
name2 = input().split()
partners = {}
for i in range(N):
    partners[name1[i]] = name2[i]
Flag = True
for i in range(N):
    if name1[i] == partners[name1[i]] or name1[i] != partners[partners[name1[i]]]:
        Flag = False
        break
if Flag:
    print("good")
else:
    print("bad")
