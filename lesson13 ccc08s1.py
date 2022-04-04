# https://dmoj.ca/problem/ccc08s1

temps = []
cold = {}
while True:
    n = input().split()
    temps.append(int(n[1]))
    cold[n[1]] = n[0]
    if n[0] == "Waterloo":
        break
temps.sort()
print(cold[str(temps[0])])
