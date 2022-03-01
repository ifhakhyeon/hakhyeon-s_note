import sys
input = sys.stdin.readline

# f = open(r"C:\Users\H30208\Desktop\조학현 공부노트\input.txt", 'r')
N = int(input())
# N = int(f.readline())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))
    # paper.append(list(map(int, f.readline().split())))
# f.close()

def zeroone(list, N, type):
    testlist = [[type for _ in range(N)] for _ in range(N)]
    if list == testlist:
        return type
    else:
        return None

def count(paper, N):
    zero = 0
    one = 0
    mone = 0

    type = paper[0][0]
    if zeroone(paper, N, type) == type:
        if type == -1:
            return 1, 0, 0
        elif type == 0:
            return 0, 1, 0
        elif type == 1:
            return 0, 0, 1

    rangelist = [0, N//3, 2*N//3, N]
    for i in range(3):
        for j in range(3):
            test = [row[rangelist[j]: rangelist[j+1]] for row in paper[rangelist[i]: rangelist[i+1]]]
            m, z, o = count(test, N // 3)
            mone += m
            zero += z
            one += o
    return mone, zero, one


if __name__ == '__main__':
    a, b, c = count(paper, N)
    print(a)
    print(b)
    print(c)