# https://dmoj.ca/problem/ccc03s1

piece = 1
while True:
    n = int(input())
    if piece + n != 100 and n != 0 and n != 1:
        if piece + n == 54:
            piece = 19
        elif piece + n == 90:
            piece = 48
        elif piece + n == 99:
            piece = 77
        elif piece + n == 9:
            piece = 34
        elif piece + n == 40:
            piece = 64
        elif piece + n == 67:
            piece = 86
        elif piece + n > 100:
            piece = piece
        else:
            piece = piece + n
        print("You are now on square", piece)
    elif piece + n == 100:
        print("You are now on square 100")
        print("You Win!")
        break
    elif n == 0 or n == 1:
        print("You Quit!")
        break
