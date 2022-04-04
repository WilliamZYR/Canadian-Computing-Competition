# https://dmoj.ca/problem/ccc02s1

pink = int(input())
green = int(input())
red = int(input())
orange = int(input())
money = int(input())
count = 0
maximum = money//pink+1
minimum = maximum
for i in range(maximum):
    for j in range(maximum):
        for k in range(maximum):
            for l in range(maximum):
                if (pink * i + green * j + red * k + orange * l == money):
                    print("# of PINK is", i, "# of GREEN is", j, "# of RED is", k, "# of ORANGE is", l)
                    count = count + 1
                    if i+j+k+l < minimum:
                        minimum = i+j+k+l
                    else:
                        minimum = minimum
print("Total combinations is "+str(count)+".")
print("Minimum number of tickets to print is "+str(minimum)+".")


