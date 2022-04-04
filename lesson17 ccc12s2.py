# https://dmoj.ca/problem/ccc12s2

AR = input()
A = []
R = []
dictionary = {}
dictionary["I"] = 1
dictionary["V"] = 5
dictionary["X"] = 10
dictionary["L"] = 50
dictionary["C"] = 100
dictionary["D"] = 500
dictionary["M"] = 1000
for i in range(len(AR)//2):
    A.append(int(AR[2*i]))
    R.append(dictionary[AR[2*i+1]])
value = 0
for i in range(len(R)-1):
    if R[i] < R[i+1]:
        value = value - R[i]*A[i]
    else:
        value = value + R[i]*A[i]
value = value + R[-1]*A[-1]
print(value)
