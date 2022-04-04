# https://dmoj.ca/problem/ccc00s1

quarters = int(input())
A = int(input())
B = int(input())
C = int(input())
times = 0
for i in range(0, 100000, 1):
    times = times + 1
    if (i%105 == (35-A-1)*3+1):
        quarters = quarters + 30
    if (i%300 == (100-B-1)*3+2):
        quarters = quarters + 60
    if (i%30 == (10-C-1)*3+3):
        quarters = quarters + 9
    quarters = quarters - 1
    if (quarters == 0):
        break
print("Martha plays", times, "times before going broke.")
