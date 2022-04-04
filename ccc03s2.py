# https://dmoj.ca/problem/ccc03s2

number = int(input())
for i in range(number):
    syllables = []
    for j in range(4):
        line = input().split()
        word = line[-1]
        if 'a' in word or 'e' in word or 'i' in word or 'o' in word or 'u' in word:
            for k in range(len(word)):
                if word[-k-1] == 'a' or word[-k-1] == 'e' or word[-k-1] == 'i' or word[-k-1] == 'o' or word[-k-1] == 'u':
                    syllables.append(word[-k-1:])
                    break
        else:
            syllables.append(word)
    if syllables[0] == syllables[1] == syllables[2] == syllables[3]:
        print("perfect")
    elif syllables[0] == syllables[1] and syllables[2] == syllables[3]:
        print("even")
    elif syllables[0] == syllables[2] and syllables[1] == syllables[3]:
        print("cross")
    elif syllables[0] == syllables[3] and syllables[1] == syllables[2]:
        print("shell")
    else:
        print("free")
