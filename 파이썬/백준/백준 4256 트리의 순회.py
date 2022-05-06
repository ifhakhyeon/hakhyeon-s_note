import sys
input = sys.stdin.readline
sys.setrecursionlimit(7*(10**5))

C = int(input())


def post_order(in_s, in_e, p_s, p_e):
    if in_s > in_e or p_s > p_e:
        return
    root = preorder[p_s]

    # print('??', in_s, in_e, p_s, p_e, root)
    root_idx = position[root]
    # print('???', root_idx)

    left = root_idx - in_s
    right = in_e - root_idx

    post_order(in_s, in_s + left - 1, p_s + 1, p_s + left)

    post_order(in_e - right + 1, in_e, p_e - right + 1, p_e)
    print(root, end=' ')


for k in range(C):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))

    position = [0] * (n+1)
    for i in range(n):
        position[inorder[i]] = i

    post_order(0, n-1, 0, n-1)
    print()