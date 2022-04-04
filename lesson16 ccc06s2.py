# https://dmoj.ca/problem/ccc06s2

plaintext = input()
ciphertext = input()
ruby = {}
for i in range(len(plaintext)):
    ruby[ciphertext[i]] = plaintext[i]
new = input()
for i in range(len(new)):
    if new[i] in ruby:
        print(ruby[new[i]], end="")
    else:
        print(".", end="")
