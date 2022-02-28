import sys
input = sys.stdin.readline

# f = open(r"C:\Users\H30208\Desktop\조학현 공부노트\input.txt", 'r')
N = int(input())
# N = int(f.readline())
paper = []
for _ in range(N):
    paper.append(input().strip())
    # paper.append(f.readline().strip())
# f.close()

def zeroone(list, N):
    zerolist = ['0'*N for _ in range(N)]
    onelist = ['1'*N for _ in range(N)]
    if list == zerolist:
        return '0'
    elif list == onelist:
        return '1'
    else:
        return '-1'

def count(paper, N):
    ret = ''
    if N == 1:
        if paper[0][0] == '1':
            return '1'
        elif paper[0][0] == '0':
            return '0'

    if zeroone(paper, N) == '1':
        return '1'
    elif zeroone(paper, N) == '0':
        return '0'

    ret = '('

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
        c = zeroone(i, N//2)
        if c == 0:
            ret += '0'
        elif c == 1:
            ret += '1'
        else:
            ret += count(i, N // 2)
    ret += ')'
    return ret


if __name__ == '__main__':
    print(count(paper, N))


