#https://dmoj.ca/problem/ccc00s2

number = int(input())
stream = []
for i in range(0, number, 1):
    stream.append(float(input()))
while (True):
    indicator = input()
    if (indicator == "99"):
        which = int(input())
        percentage = int(input())
        stream.insert(which, stream[which - 1] * (100 - percentage) / 100)
        stream[which - 1] = stream[which - 1] * percentage / 100
    if (indicator == "88"):
        which = int(input())
        stream[which-1] = stream[which - 1] + stream[which]
        stream.pop(which)
    if (indicator == "77"):
        break
for i in range(len(stream)):
    print(int((stream[i])), end=" ")
print()


