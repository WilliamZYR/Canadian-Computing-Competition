# https://dmoj.ca/problem/ccc10s2

k = int(input())
dictionary = {}
for i in range(k):
    character, digits = map(str, input().split())
    dictionary[digits] = character
code = input()
plaintext = ''

while True:

    if len(code) >= 10:
        for i in range(0, 11, +1):
            if code[0:i] in dictionary:
                code = code[i:]
                plaintext = plaintext + dictionary[code[0:i]]
                break

    elif 0 < len(code) < 10:
        for i in range(0, len(code)+1, +1):
            if code[0:i] in dictionary:
                code = code[i:]

                break

    elif len(code) == 0:
        break

print(plaintext)
