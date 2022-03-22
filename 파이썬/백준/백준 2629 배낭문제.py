import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# f = open(r"C:\Users\H30208\Desktop\조학현 공부노트\input.txt", 'r')
# N = int(f.readline())
N = int(input())
# q = list(map(int, f.readline().split()))
numlist = list(map(int, input().split()))
C = int(input())
# C = int(f.readline())

# cache[현제 idx][targetnum]
cache = [[-1 for _ in range(40001)] for i in range(N)]

def peek(idx, target):
    if target > sum(numlist[idx:]) or target < -sum(numlist[idx:]):
        return 0
    if target == 0:
        return 1
    if idx == N:
        return 0
    if cache[idx][target] != -1:
        return cache[idx][target]

    ret = peek(idx+1, target) or peek(idx+1, target + numlist[idx]) or peek(idx+1, target - numlist[idx])
    cache[idx][target] = ret

    return ret

check = list(map(int, input().split()))
for i in check:
    if peek(0, i):
        print('Y')
    else:
        print('N')
