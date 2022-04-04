# https://dmoj.ca/problem/ccc05s2

c, r = map(int, input().split())
x = 0
y = 0
while(True):
    a, b = map(int, input().split())
    x = x + a
    y = y + b
    if (a==0 and b==0):
        break
    elif (x<=c and y<=r):
        print(x,y)
    elif (x>c and y<=r):
        x = c
        print(x,y)
    elif (x<=c and y>r):
        y = r
        print(x,y)
    elif(x>c and y>r):
        x = c
        y = r
        print(x,y)

    if (a == 0 and b == 0):
        break
    if (x < 0):
        x = 0
    if (x > c):
        x = c
    if (y < 0):
        y = 0
    if (y > r):
        y = r
    print(x, y)

    # x is independent from y
