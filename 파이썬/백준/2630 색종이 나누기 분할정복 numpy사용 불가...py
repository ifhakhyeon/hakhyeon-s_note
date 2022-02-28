import sys
input = sys.stdin.readline
import numpy as np

# f = open(r"C:\Users\H30208\Desktop\조학현 공부노트\input.txt", 'r')
N = int(input())
# N = int(f.readline())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))
    # paper.append(list(map(int, f.readline().split())))
# f.close()
paper = np.array(paper)

def zeroone(list):
    if 0 not in list:
        return 1
    elif 1 not in list:
        return 0
    elif 0 in list and 1 in list:
        return -1
def count(paper, N):
    zero = 0
    one = 0
    ul = paper[0:N//2, 0:N//2]
    ur = paper[0:N//2, N//2:]
    ll = paper[N//2:, 0:N//2]
    lr = paper[N//2:, N//2:]

    for i in ul, ur, ll, lr:
        c = zeroone(i)
        if c == 0:
            zero += 1
        elif c == 1:
            one += 1
        else:
            z, o = count(i, N//2)
            zero += z
            one += o
    return zero, one

if __name__ == '__main__':
    a, b = count(paper, N)
    print(a)
    print(b)