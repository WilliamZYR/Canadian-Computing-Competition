# https://dmoj.ca/problem/ccc04s2

n, k = map(int, input().split())

scoreKeeper = [[0 for j in range(n)] for i in range(k)]
rank = [[0 for j in range(n)] for i in range(k)]

line = list(map(int, input().split()))
for i in range(n):
    scoreKeeper[0][i] = line[i]
sortedList = sorted(scoreKeeper[0], reverse=True)
for i in range(n):
    rank[0][i] = sortedList.index(scoreKeeper[0][i]) + 1

for j in range(1, k):
    line = list(map(int, input().split()))
    for i in range(n):
        scoreKeeper[j][i] = line[i] + scoreKeeper[j - 1][i]
    sortedList = sorted(scoreKeeper[j], reverse=True)
    for i in range(n):
        rank[j][i] = sortedList.index(scoreKeeper[j][i]) + 1

winners = []
for i in range(n):
    if (rank[k - 1][i] == 1):
        winners.append(i)

for winner in winners:
    worstRank = 1
    for i in range(k):
        worstRank = max(worstRank, rank[i][winner])

    print("Yodeller", winner, "is the TopYodeller: score", scoreKeeper[k - 1][winner], ", worst rank", worstRank)
