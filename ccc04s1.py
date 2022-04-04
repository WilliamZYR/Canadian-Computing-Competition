# https://dmoj.ca/problem/ccc04s1

number = int(input())
for i in range(number):
    words = []
    for j in range(3):
        words.append(input())

    flag = True
    for j in range(3):  # j represents the first word
        for k in range(3):  # k represents the second word
            # I want to check if word[j] is a prefix / suffix of word[k]
            if (j != k and len(words[j]) <= len(words[k])):
                if (words[j] == words[k][: len(words[j])] or words[j] == words[k][-len(words[j]):]):
                    flag = False
    if flag is True:
        print("Yes")
    else:
        print("No")
