# https://dmoj.ca/problem/ccc07s1

n = int(input())
for i in range(n):
    y, m, d = map(int, input().split())
    if y <= 1988:
        print("Yes")
        pass
    elif y >= 1990:
        print("No")
        pass
    else:
        if m == 1:
            print("Yes")
            pass
        elif m >= 3:
            print("No")
            pass
        else:
            if d <= 27:
                print("Yes")
                pass
            else:
                print("No")
