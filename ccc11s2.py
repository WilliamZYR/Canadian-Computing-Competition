# https://dmoj.ca/problem/ccc11s2

N = int(input())
student = []
for i in range(N):
    student.append(input())
correct = []
for i in range(N):
    correct.append(input())
count = 0
for i in range(N):
    if student[i] == correct[i]:
        count += 1
print(count)
