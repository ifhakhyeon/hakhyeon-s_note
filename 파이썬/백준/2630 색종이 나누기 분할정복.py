import sys

input = sys.stdin.readline

f = open(r"C:\Users\H30208\Desktop\조학현 공부노트\input.txt", 'r')
# N = int(input())
N = int(f.readline())
paper = []
for _ in range(N):
    # paper.append(list(map(int, input().split())))
    paper.append(list(map(int, f.readline().split())))
f.close()

# paper = np.array(paper)

def zeroone(list, N):
    zerolist = [[0 for _ in range(N)] for _ in range(N)]
    onelist = [[1 for _ in range(N)] for _ in range(N)]
    if list == zerolist:
        return 0
    elif list == onelist:
        return 1
    else:
        return -1


def count(paper, N):
    zero = 0
    one = 0
    # if N == 1:
    #     if paper[0][0] == 1:
    #         return 0, 1
    #     elif paper[0][0] == 0:
    #         return 1, 0
    #     else:
    #         return 0, 0

    if zeroone(paper, N) == 1:
        return 0, 1
    elif zeroone(paper, N) == 0:
        return 1, 0
    else:
        pass

    ul = []
    for i in range(N // 2):
        ul.append(paper[i][0:N // 2])
    ur = []
    for i in range(N // 2):
        ur.append(paper[i][N // 2:])
    ll = []
    for i in range(N // 2, N):
        ll.append(paper[i][0:N // 2])
    lr = []
    for i in range(N // 2, N):
        lr.append(paper[i][N // 2:])

    for i in ul, ur, ll, lr:
        c = zeroone(i, N // 2)
        if c == 0:
            zero += 1
        elif c == 1:
            one += 1
        else:
            z, o = count(i, N // 2)
            zero += z
            one += o

    return zero, one


if __name__ == '__main__':
    a, b = count(paper, N)
    print(a)
    print(b)
    # print(N)
    # for i in paper:
    #     print(i)
    # print()
    # for i in ul:
    #     print(i)
    # print()
    # for i in ur:
    #     print(i)
    # print()
    # for i in ll:
    #     print(i)
    # print()
    # for i in lr:
    #     print(i)
