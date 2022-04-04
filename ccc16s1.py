# https://dmoj.ca/problem/ccc16s1

first = input()
second = input()
characters1 = list(first)
characters2 = list(second)
flag = True
for i in range(len(characters2)):
    if characters2[i] == '*':
        continue
    else:
        if characters2[i] in characters1:
            characters1.remove(characters2[i])
        else:
            flag = False
            break
if flag:
    print("A")
if not flag:
    print("N")

