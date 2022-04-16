def calc(arr, n):
    if n == 1:
        return [1]

    mod = 10 ** 9 + 7
    ans = [0] * n
    ans[0] = 1
    ans[1] = min(arr[0], arr[1])
    stack = [(ans[1], 1)]
    for i in range(2, n):
        x = min(arr[i - 1], arr[i])
        y = 0
        ans[i] = ans[i - 1] * (x + 1) % mod
        while stack and (stack[-1][0] >= x):
            xx, yy = stack.pop()
            ans[i] = (ans[i] - yy * (xx - x)) % mod
            y += yy
        stack.append((x, y + ans[i - 1]))
    return ans

def calc_1(v, N):
    if N == 1:
        return [1]
    mod = 10**9 + 7
    psum = [0] * (N+2); psum[0] = 1
    ans = [0] * N; ans[0] = 1
    m = min(v[0], v[1])
    ans[1] = m
    psum[1] = 1 + m
    # [min, start, end] // (psum[end] - psum[start]) part sum form start+1 to end
    cache = [[m, -1, 0]]
    for i in range(2, N):
        if v[i] >= v[i-1]:
            cache.append([v[i-1], i-2, i-1])
            ans[i] = (ans[i-1] + ((ans[i-1] * v[i-1]) % mod)) % mod

        elif v[i] < v[i-1]:
            start = i-2
            end = i-1
            while cache and cache[-1][0] >= v[i]:
                start = cache.pop()[1]
            cache.append([v[i], start, end])
            ret = 0
            # print(cache)
            for k in cache:
                ret += (k[0] * (psum[k[2]] - psum[k[1]])) % mod
            ans[i] = ret % mod
        psum[i] = (psum[i - 1] + ans[i]) % mod
    return ans

# N = int(input())
# v = list(map(int, input().split()))

v = [1, 2, 3]
# v = [1, 3, 4, 2, 1]
# v = [1, 5, 4, 3, 2]
# v = [1,2,3,4,5,6,7,8]
# v = [random.randint(1, 1000000001) for _ in range(1000)]
# for i in v:
#     print(i)
N = len(v)
ans = calc(v, N)
ans1 = calc_1(v, N)
for i in range(N):
    print(ans[i], ans1[i], ans[i] == ans1[i])