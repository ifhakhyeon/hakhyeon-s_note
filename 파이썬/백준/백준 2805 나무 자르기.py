import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree = list(map(int, input().split()))

def cut(m):
    a = list(map(lambda x: x-m if (x-m > 0) else 0, tree))
    return sum(a)

def set_meter(start, end):
    if start == end:
        return start
    if start+1 == end:
        return end if cut(end) >= M else start
    mid = (start + end)//2
    if cut(mid) > M:
        return set_meter(mid, end)
    else:
        return set_meter(start, mid)

print(set_meter(0, max(tree)))