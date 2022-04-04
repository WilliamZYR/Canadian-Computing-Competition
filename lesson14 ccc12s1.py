# https://dmoj.ca/problem/ccc12s1

'''
J = int(input())
count = 0
if J - 1 == 3:
    count = 0
if J - 1 > 3:
    for i in range(3, J, +1):
        if i == 3:
            count += 1
        elif i > 3:
            for j in range(2, i, +1):
                if j == 2:
                    count += 1
                elif j > 2:
                    for k in range(1, j, +1):
                        count += 1
print(count)
'''


J = int(input())
print((J-1)(J-2)(J-3) / 6) # the number of combinations (J - 1)C3
    # (J - 1)P3 / 3!
    # (J - 1)P3 == (J-1)(J-2)(J-3)
    # ==> (J - 1)C3 = (J - 1)P3 / 3! = (J-1)(J-2)(J-3) / 6