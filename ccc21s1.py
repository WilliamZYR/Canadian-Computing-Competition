N = int(input())
heights = list(map(int, input().split()))
widths = list(map(int, input().split()))
area = 0
for i in range(N):
    area += (heights[i] + heights[i+1]) * widths[i] / 2
print(area)
