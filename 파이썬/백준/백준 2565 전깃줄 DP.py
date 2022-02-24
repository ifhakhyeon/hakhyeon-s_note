n = int(input())
line = []
for _ in range(n):
    line.append(list(map(int, input().split())))

line.sort(key=lambda x: x[0])
cache = [-1 for _ in range(n + 1)]

# type == 0 -> lineL / type == 1 -> lineR
def lis2(start):
    if cache[start] != -1:
        return cache[start]

    cache[start] = 1

    for i in range(start+1, n):
        if line[start][1] < line[i][1] and line[start][0] < line[i][0]:
            cache[start] = max(cache[start], lis2(i) + 1)

    return cache[start]

ret = 0
for i in range(n):
    ret = max(ret, lis2(i))

print(n-ret)
