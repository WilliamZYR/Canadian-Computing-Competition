# https://dmoj.ca/problem/ccc06s1

mother = input()
father = input()
together = ''
for i in range(10):
    together = together + mother[i] + father[i]
countA = 0
countB = 0
countC = 0
countD = 0
countE = 0
for i in range(20):
    if together[i] == 'A':
        countA += 1
    if together[i] == 'B':
        countB += 1
    if together[i] == 'C':
        countC += 1
    if together[i] == 'D':
        countD += 1
    if together[i] == 'E':
        countE += 1
count = [countA, countB, countC, countD, countE]
letters = ['a', 'b', 'c', 'd', 'e']
LETTERS = ['A', 'B', 'C', 'D', 'E']
number = int(input())
for i in range(number):
    baby = input()
    Possible = True
    for j in range(5):
        if count[j] == 0 and baby[j] == letters[j]:
            Possible = True
        elif count[j] == 1 or count[j] == 2 and baby[j] == letters[j]:
            Possible = True
        elif count[j] == 1 or count[j] == 2 and baby[j] == LETTERS[j]:
            Possible = True
        elif count[j] == 3 or count[j] == 4 and baby[j] == LETTERS[j]:
            Possible = True
        else:
            Possible = False
            break

    if Possible == True:
        print("Possible baby.")
    if Possible == False:
        print("Not their baby!")
'''

m = input()
f = input()

ps = []  # ps stands for PossibilitieS
for i in range(5):
    ps.append([])
    ps[i].append(min(m[2 * i], f[2 * i]))
    ps[i].append(min(m[2 * i], f[2 * i + 1]))
    ps[i].append(min(m[2 * i + 1], f[2 * i]))
    ps[i].append(min(m[2 * i + 1], f[2 * i + 1]))

for row in ps:
    print(row)

X = int(input())
for x in range(X):
    c = input()
    flag = True
    for i in range(5):
        if (c[i] not in ps[i]):
            flag = False
            break
    if (flag):
        print("Possible baby.")
    else:
        print("Not their baby!")
'''

mother = input()
father = input()
together = mother + father
countA = 0
countB = 0
countC = 0
countD = 0
countE = 0
for i in range(20):
    if together[i] == 'A':
        countA += 1
        if (i < 19 and together[i] == together[i + 1]):
            countA += 1
    if together[i] == 'B':
        countB += 1
        if (i < 19 and together[i] == together[i + 1]):
            countB += 1
    if together[i] == 'C':
        countC += 1
        if (i < 19 and together[i] == together[i + 1]):
            countC += 1
    if together[i] == 'D':
        countD += 1
        if (i < 19 and together[i] == together[i + 1]):
            countD += 1
    if together[i] == 'E':
        countE += 1
        if (i < 19 and together[i] == together[i + 1]):
            countE += 1

count = [countA, countB, countC, countD, countE]
letters = ['a', 'b', 'c', 'd', 'e']
LETTERS = ['A', 'B', 'C', 'D', 'E']
number = int(input())
for i in range(number):
    baby = input()
    Possible = True
    for j in range(5):
        if count[j] == 0 and baby[j] == letters[j]:
            Possible = True
        elif count[j] == 1 or count[j] == 2 and baby[j] == letters[j]:
            Possible = True
        elif count[j] == 1 or count[j] == 2 and baby[j] == LETTERS[j]:
            Possible = True
        elif count[j] >= 3 and baby[j] == LETTERS[j]:
            Possible = True
        else:
            Possible = False
            break

    if Possible == True:
        print("Possible baby.")
    if Possible == False:
        print("Not their baby!")
