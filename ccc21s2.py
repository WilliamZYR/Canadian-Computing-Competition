
M = int(input())
N = int(input())
K = int(input())
R = 0
C = 0
count = 0
Rchoices = [0 for i in range(M)]
Cchoices = [0 for i in range(N)]
for i in range(K):
    type, num = map(str, input().split())
    num = int(num)
    if type == 'R':
        if Rchoices[num-1] == 0:
            Rchoices[num - 1] = num
            R += 1
            count += (N - C)
            count -= C
        elif Rchoices[num-1] == num:
            Rchoices[num - 1] = 0
            R -= 1
            count += C
            count -= (N - C)
    elif type == 'C':
        if Cchoices[num - 1] == 0:
            Cchoices[num - 1] = num
            C += 1
            count += (M - R)
            count -= R
        elif Cchoices[num-1] == num:
            Cchoices[num - 1] = 0
            C -= 1
            count += R
            count -= (M - R)
print(count)
