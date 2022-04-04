#

n = int(input())
box = []
item = []
for i in range(n):
    a, b, c = map(int, input().split())
    size1 = [a, b, c]
    size1.sort()
    box.append(size1)
m = int(input())
for i in range(m):
    a, b, c = map(int, input().split())
    size2 = [a, b, c]
    size2.sort()
    item.append(size2)

volume = 8000000000

for i in range(m):
    for j in range(n):
        for k in range(3):
            if item[i][k] <= box[j][k]:
                if item[i][0]*item[i][1]*item[i][2] < volume:
                    volume = item[i][0]*item[i][1]*item[i][2]
                else:
                    volume = volume + 0
        print(volume)



for i in range(m):
    hasFound = False  # have we found a box where the item will fit?
    volume = 0
    for j in range(n):

        boxVolume = box[j][0] * box[j][1] * box[j][2]

        if (item[i][0] <= box[j][0] and item[i][1] <= box[j][1] and item[i][2] <= box[j][2]):
            if (not hasFound):  # if we haven't found any, then this is the first box that will fit the item
                volume = boxVolume
            else:
                volume = min(volume, boxVolume)
            hasFound = True

    if (hasFound):
        print(volume)
    else:
        print("Item does not fit.")

