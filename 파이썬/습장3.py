import sys
input = sys.stdin.readline

n, c = map(int, input().split())
stuff = list(map(int, input().split()))
l_stuff = stuff[n//2:]
r_stuff = stuff[:n//2]

lsum = []
rsum = []


def find(s, _sum, length, weight):
    if length >= len(s):
        _sum.append(weight)
        return
    find(s, _sum, length+1, weight)
    find(s, _sum, length+1, weight+s[length])


def search(arr, target, start, end):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] <= target:
            start = mid+1
        else:
            end = mid
    return end


find(l_stuff, lsum, 0, 0)
find(r_stuff, rsum, 0, 0)
lsum.sort()

ans = 0
for i in rsum:
    if c < i:
        continue
    ans += search(lsum, c-i, 0, len(lsum))

print(ans)