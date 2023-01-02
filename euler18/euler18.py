import sys

data = sys.stdin.readlines()
data = [[int(n) for n in e.split()] for e in data]

root = data[0][0]

for i in range(len(data) - 2, 0, -1):
    for j in range(len(data[i])):
        data[i][j] = data[i][j] + max(data[i+1][j], data[i+1][j+1])

ans = root + max(data[1][0], data[1][1])

print(ans)