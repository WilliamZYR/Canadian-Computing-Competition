# https://dmoj.ca/problem/ccc17s2

N = int(input())
tide = input().split()
for i in range(N):
    tide[i] = int(tide[i])
tide.sort()
low = []
high = []
if len(tide) % 2 == 0:
    low = tide[0:len(tide)//2]
    high = tide[len(tide)//2:]
    for i in range(len(tide) // 2):
        print(low[-i - 1], end=" ")
        print(high[i], end=" ")
elif len(tide) % 2 == 1:
    low = tide[0:len(tide)//2+1]
    high = tide[len(tide)//2+1:]
    for i in range(len(tide) // 2):
        print(low[-i - 1], end=" ")
        print(high[i], end=" ")
    print(low[0])
