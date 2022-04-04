# https://dmoj.ca/problem/ccc10s1

n = int(input())
if n == 0:
    print("")
elif n == 1:
    name, r, s, d = map(str, input().split())
    print(name)
elif n >= 2:

    values = set()
    mapping = {}
    for i in range(n):
        name, r, s, d = map(str, input().split())
        R = int(r)
        S = int(s)
        D = int(d)
        value = 2 * R + 3 * S + D
        values.add(value)
        if (value not in mapping):
            mapping[value] = [name]
        else:
            mapping[value].append(name)
    values = list(values)
    values.sort(reverse=True)

    potentialNames = mapping[values[0]]
    potentialNames.sort()
    print(potentialNames[0])
    if len(potentialNames) >= 2:
        print(potentialNames[1])
    else:
        potentialNames2 = mapping[values[1]]
        potentialNames2.sort()
        print(potentialNames2[0])