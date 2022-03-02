import sys
input = sys.stdin.readline
# key = lambda x: x[1]
# sys.setrecursionlimit(10 ** 6)

# f = open(r"C:\Users\H30208\Desktop\조학현 공부노트\input.txt", 'r')
# C = int(f.readline())
C = int(input())
# list = list(map(int, f.readline().split()))
for _ in range(C):
    # N = int(f.readline())
    N = int(input())
    # length = list(map(int, f.readline().split()))
    length = list(map(int, input().split()))
    ret = 0
    while True:
        # print(length)
        # print(ret)
        minnum1 = min(length)
        length.remove(minnum1)
        minnum2 = min(length)
        length.remove(minnum2)
        a = minnum1 + minnum2
        ret += a
        if not length:
            break
        length.append(a)
    print(ret)