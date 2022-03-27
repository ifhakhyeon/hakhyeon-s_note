import sys
input = sys.stdin.readline
# arr = [1,2,3,4,5] 일 때 start, end, node
#                                     ↙ 0 4 1 ↘
#                      ↙ 2 2 6 ↘                      ↙ 3 4 3 ↘
#             ↙ 0 1 4 ↘          2 2 5           3 3 6        4 4 7
#         0 0 8         1 1 9
#
#

def init(arr, tree, start, end, node):
    # leaf 노드 라는 의미
    # 그냥 그 값을 저장
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        init(arr, tree, start, mid, node * 2)
        init(arr, tree, mid + 1, end, node * 2 + 1)
        # 재귀가 끝나고 값(합)을 저장함
        tree[node] = tree[node * 2] + tree[node * 2 + 1]


def update_lazy(tree, lazy, node, start, end):
    if lazy[node] != 0:
        tree[node] += (end - start + 1) * lazy[node]
        if start != end:
            lazy[node * 2] += lazy[node]
            lazy[node * 2 + 1] += lazy[node]
        lazy[node] = 0


def update_range(tree, lazy, start, end, node, idx_start, idx_end, dif):
    update_lazy(tree, lazy, node, start, end)
    # 의미 없음!
    if idx_start > end or start > idx_end:
        return

    # 구간을 포함하고 있으면 정확하게 +를 해주고 lazy를 물려줌
    if start >= idx_start and idx_end >= end:
        tree[node] += (end - start + 1) * dif
        if start != end:
            lazy[node * 2] += dif
            lazy[node * 2 + 1] += dif
        return

    # 일부만 포함할 수도 있으니 update를 다시 실행해줌
    mid = (start + end) // 2
    update_range(tree, lazy, start, mid, node * 2, idx_start, idx_end, dif)
    update_range(tree, lazy, mid + 1, end, node * 2 + 1, idx_start, idx_end, dif)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]


def sum(tree, lazy, start, end, node, left, right):
    update_lazy(tree, lazy, node, start, end)
    # 구간을 벗어나면 0을 return
    if left > end or start > right:
        return 0
    # 구간이 전부 포함되면 그 노드를 리턴
    if start >= left and right >= end:
        return tree[node]

    mid = (start + end) // 2
    return sum(tree, lazy, start, mid, node * 2, left, right) + sum(tree, lazy, mid + 1, end, node * 2 + 1, left, right)


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    arr = [int(input()) for _ in range(n)]
    val = [list(map(int, input().split())) for _ in range(m + k)]
    # tree_list=[0]*(pow(2,math.ceil(math.log(n,2))+1)-1)
    tree_list = [0] * (n * 4)
    lazy = [0] * (n * 4)
    init(arr, tree_list, 0, n - 1, 1)

    for v in val:
        b, c = v[1], v[2]
        if v[0] == 1:  # b~c까지 d를 더함
            d = v[3]
            update_range(tree_list, lazy, 0, n - 1, 1, b - 1, c - 1, d)
        else:
            print(sum(tree_list, lazy, 0, n - 1, 1, b - 1, c - 1))