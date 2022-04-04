numbers = [[1, 2], [3, 4]]
flips = input()

for i in range(len(flips)):
    if flips[i] == "H":
       numbers.append(numbers[0])
       del numbers[0]
    else:
        numbers[0].append(numbers[0][0])
        numbers[1].append(numbers[1][0])
        del numbers[0][0]
        del numbers[1][0]
for i in range(2):
    for j in range(2):
        print(numbers[i][j], end=" ")
    print()
