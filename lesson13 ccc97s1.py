# https://dmoj.ca/problem/ccc97s1
Set = int(input())
for i in range(Set):
    nsubjects = int(input())
    nverbs = int(input())
    nobjects = int(input())
    subjects = []
    verbs = []
    objects = []
    for j in range(nsubjects):
        subjects.append(input())
    for j in range(nverbs):
        verbs.append(input())
    for j in range(nobjects):
        objects.append(input())
    for j in range(nsubjects):
        for k in range(nverbs):
            for l in range(nobjects):
                print(subjects[j], verbs[k], objects[l] + ".")