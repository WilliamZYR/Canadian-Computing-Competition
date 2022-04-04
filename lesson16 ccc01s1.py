# https://dmoj.ca/problem/ccc01s1

cards = input()
clubs = ""
diamonds = ""
hearts = ""
spades = ""
for i in range(17):
    if cards[i] == 'C':
        for j in range(i+1, 17, +1):
            if cards[j] != 'D':
                clubs += cards[j] + ' '
            else:
                break
    if cards[i] == 'D':
        for j in range(i+1, 17, +1):
            if cards[j] != 'H':
                diamonds += cards[j] + ' '
            else:
                break
    if cards[i] == 'H':
        for j in range(i+1, 17, +1):
            if cards[j] != 'S':
                hearts += cards[j] + ' '
            else:
                break
    if cards[i] == 'S':
        for j in range(i+1, 17, +1):
            spades += cards[j] + ' '
point1 = 0
point2 = 0
point3 = 0
point4 = 0
points = [point1, point2, point3, point4]
suits = [clubs, diamonds, hearts, spades]
for i in range(4):
    if len(suits[i]) == 0:
        points[i] += 3
    elif len(suits[i]) == 2:
        points[i] += 2
    elif len(suits[i]) == 4:
        points[i] += 1
    for j in range(len(suits[i])):
        if suits[i][j] == 'J':
            points[i] += 1
        elif suits[i][j] == 'Q':
            points[i] += 2
        elif suits[i][j] == 'K':
            points[i] += 3
        elif suits[i][j] == 'A':
            points[i] += 4
print("Cards Dealt              Points")
print("Clubs", suits[0], points[0])
print("Diamonds", suits[1], points[1])
print("Hearts", suits[2], points[2])
print("Spades", suits[3], points[3])
print("          Total", sum(points))
