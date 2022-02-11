def least(num):
    return int((2 * num) ** (1 / 2))
def point(cacheD, cacheG, Dscore, Gscore, type):
    if type == 'D':
        trdscore = 987654321
        for i in cacheD:
            if i == -1:
                trdscore = 1000
                break
            if i < trdscore:
                trdscore = i
        ret = Dscore + trdscore
        return ret

    if type == 'G':
        trdscore = 987654321
        for i in cacheG:
            if i == -1:
                trdscore = 1000
                break
            if i < trdscore:
                trdscore = i
        ret = Gscore + trdscore
        return ret

list = [True for _ in range((500000) + 1)]

cacheD = [-1 for _ in range(3)]
cacheG = [-1 for _ in range(3)]
Maxcall = -1
C = int(input())
Dscore = 0
Gscore = 0

for _ in range(C):
    Daewoong, Gueseong = map(int, (input().split()))

    if Daewoong == 0 or Daewoong == 1:
        point(cacheD, cacheG, Dscore, Gscore, 'G')
    if Gueseong == 0 or Gueseong == 1:
        point(cacheD, cacheG, Dscore, Gscore, 'D')
# -----
    if Maxcall < N:

        least_N = least(N)

        for i in range(2, least_N + 1):
            if list[i] == True:
                for j in range(2 * i, 2 * N + 1, i):
                    list[j] = False

        sum = 0
        for i in range(N + 1, 2 * N + 1):
            if i == 1 or i == 0:
                continue
            if list[i] == True:
                sum += 1
        print(sum)
        Maxcall = N

    else:
        sum = 0
        for i in range(N + 1, 2 * N + 1):
            if i == 1 or i == 0:
                continue
            if list[i] == True:
                sum += 1
        print(sum)

# https://www.acmicpc.net/problem/14622