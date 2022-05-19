import sys
from collections import defaultdict
input = sys.stdin.readline

w = int(input())
word = defaultdict(list)


for _ in range(w):
    a = input().strip()
    word[a[0]].append(a)

input()
move = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))


def score(n):
    if n == 1 or n == 2:
        return 0
    elif n == 3 or n == 4:
        return 1
    elif n == 5:
        return 2
    elif n == 6:
        return 3
    elif n == 7:
        return 5
    elif n == 8:
        return 11
    else:
        return 0


def boggle(y, x, find):
    if not(0 <= y < 4 and 0 <= x < 4):
        return -9

    if board[y][x] != find[0]:
        return -9

    if len(find) == 1:
        return 1

    for M in move:
        if 0 <= y + M[0] < 4 and 0 <= x + M[1] < 4 and board[y + M[0]][x + M[1]] == find[1]:
            ss = board[y][x]
            board[y][x] = ''
            k = boggle(y + M[0], x + M[1], find[1:]) + 1
            board[y][x] = ss
            if k > 0:
                return k

    return -9


c = int(input())
for pp in range(c):
    is_find = defaultdict(bool)
    board = []
    for _ in range(4):
        k = list(input().strip())
        board.append(k)
        len_x = len(k)
    # 최대길이, 최대길이의 글자, 찾은 갯수, 점수
    ret = [-1, '', 0, 0]
    for i in range(4):
        for j in range(len_x):
            if word[board[i][j]]:
                for k in word[board[i][j]]:
                    if not is_find[k]:
                        temp = boggle(i, j, k)
                        if temp > 0:
                            is_find[k] = True
                            ret[2] += 1
                            ret[3] += score(temp)
                            if temp > ret[0]:
                                ret[0] = temp
                                ret[1] = k
                            elif temp == ret[0]:
                                ret[1] = sorted([ret[1], k])[0]

    # print(boggle(0, 0, 'ACM'))
    print(ret[3], ret[1], ret[2])
    if pp != c-1:
        input()

