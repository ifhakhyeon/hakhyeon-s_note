import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 6)

# f = open(r"C:\Users\H30208\Desktop\조학현 공부노트\input.txt", 'r')
A, B, C = map(int, input().split())
# A, B, C = map(int, f.readline().split())
# f.close()
def AexpoB(A, B):
    ret = 1
    if B == 0:
        return 1
    if B % 2 == 0:
        k = (AexpoB(A, B // 2)) % C
        ret *= (k * k) % C
    else:
        ret *= (A * AexpoB(A, B-1))
        ret %= C
    return ret
if __name__ == "__main__":
    print(AexpoB(A, B))