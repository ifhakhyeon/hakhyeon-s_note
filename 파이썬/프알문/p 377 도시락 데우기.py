import sys
input = sys.stdin.readline
# key = lambda x: x[1]

# sys.setrecursionlimit(10 ** 6)

# f = open(r"C:\Users\H30208\Desktop\조학현 공부노트\input.txt", 'r')
# C = int(f.readline())
C = int(input())

for _ in range(C):
    N = int(input())
    # N = int(f.readline())
    hottime = list(map(int, input().split()))
    # hottime = list(map(int, f.readline().split()))
    eattime = list(map(int, input().split()))
    # eattime = list(map(int, f.readline().split()))
    for i in range(N):
        eattime[i] = [i, eattime[i]]
    eattime.sort(key=lambda x : x[1])
    def eat():
        time = sum(hottime)
        ret = sum(hottime)
        for i in eattime:
            ret = max(ret, time + i[1])
            time -= hottime[i[0]]
        return ret
    if __name__ == "__main__":
        print(eat())