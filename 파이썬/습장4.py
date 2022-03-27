def calc(v, N):
    min_tree = [0 for i in range(4 * N)]
    def mintree(node, start, end):
        if start == end:
            min_tree[node] = v[start]
            return min_tree[node]
        else:
            min_tree[node] = min(mintree(node * 2, start, (start + end) // 2),
                                 mintree(node * 2 + 1, (start + end) // 2 + 1, end))
            return min_tree[node]
    mintree(1, 0, N - 1)
    def submin(node, start, end, left, right):
        if left > end or right < start:
            return 9876543210
        if left <= start and right >= end:
            return min_tree[node]
        return min(submin(node * 2, start, (start + end) // 2, left, right),
                   submin(node * 2 + 1, (start + end) // 2 + 1, end, left, right))

    def cal(v):
        m = v[-1]
        ret = 0

        for i in range(len(v)-2, -1, -1):
            m = min(m, v[i])
            ret += m * ans[i]
        return ret

    stack = [v[:i+1] for i in range(N)]
    # print(stack)
    ans = [0] * N
    ans[0] = 1
    for i in range(1, N):
        ans[i] += cal(stack[i])

    return ans

N = int(input())
v = list(map(int, input().split()))
ans = calc(v, N)

if type(ans) != list:
    print("wrong type")
else:
    for x in ans:
        print(x)
