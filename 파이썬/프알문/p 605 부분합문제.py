import sys
input = sys.stdin.readline

C = int(input())
mod = 20091101

def ans1(psum, k):
    count = [0] * K
    for i in psum:
        count[i] += 1
    ans = 0
    for i in count:
        if i >= 2:
            ans += ((i * (i - 1)) // 2) % mod
    return ans

def ans2(psum, k):
    ret = [0] * len(psum)
    prev = [-1] * k
    for i in range(len(psum)):
        if i > 0:
            ret[i] = ret[i - 1]
        else:
            ret[i] = 0

        loc = prev[psum[i]]
        if loc != -1:
            ret[i] = max(ret[i], ret[loc] + 1)
        prev[psum[i]] = i

    return ret.pop(-1)

for _ in range(C):
    N, K = map(int, input().split())
    gift = list(map(int, input().split()))
    psum = [0] * (N+1)
    psum[0] = (gift[0] % K)
    for i in range(1, N):
        psum[i] = (psum[0] + (gift[i] % K)) % K

    print(ans1(psum, K), ans2(psum, K))
