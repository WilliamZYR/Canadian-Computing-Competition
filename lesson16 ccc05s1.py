# https://dmoj.ca/problem/ccc05s1

n = int(input())
for i in range(n):
    line = input()
    num = []
    for char in line:
        if char != '-':
            num.append(char)
    for j in range(len(num)):
        if num[j] == 'A' or num[j] == 'B' or num[j] == 'C':
            num[j] = '2'
        elif num[j] == 'D' or num[j] == 'E' or num[j] == 'F':
            num[j] = '3'
        elif num[j] == 'G' or num[j] == 'H' or num[j] == 'I':
            num[j] = '4'
        elif num[j] == 'J' or num[j] == 'K' or num[j] == 'L':
            num[j] = '5'
        elif num[j] == 'M' or num[j] == 'N' or num[j] == 'O':
            num[j] = '6'
        elif num[j] == 'P' or num[j] == 'Q' or num[j] == 'R' or num[j] == 'S':
            num[j] = '7'
        elif num[j] == 'T' or num[j] == 'U' or num[j] == 'V':
            num[j] = '8'
        elif num[j] == 'W' or num[j] == 'X' or num[j] == 'Y' or num[j] == 'Z':
            num[j] = '9'
    newline = ''
    for j in range(len(num)):
        newline += num[j]
    print(newline[0:3]+"-"+newline[3:6]+"-"+newline[6:10])

