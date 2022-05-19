import sys
input = sys.stdin.readline


def update_fenwick_tree(tree, index, value):
    while index < len(tree):
        tree[index] += value
        index += (index & -index)

    return tree


def query_fenwick_tree(tree, index):
    res = 0
    while index > 0:
        res += tree[index]
        index -= (index & -index)

    return res


'''
마지막 1이 나타내는 값을 L[i]라고 표현하겠습니다.
[3] = 1, L[10] = 2, L[12] = 4이 됩니다.

수 N개를 A[1] ~ A[N]이라고 했을 때, Tree[i]는 A[i] 부터 앞으로 L[i]개의 합이 저장되어 있습니다.

L[i] = i & -i가 됩니다. 그 이유는 아래와 같습니다.
      -num = ~num + 1
       num = 100110101110101100000000000
      ~num = 011001010001010011111111111
      -num = 011001010001010100000000000
num & -num = 000000000000000100000000000
'''

if __name__ == '__main__':
    N, M, K = map(int, input().split())

    tree = [0]*(N+1)
    nums = [int(input()) for _ in range(N)]
    for i in range(N):
        tree = update_fenwick_tree(tree, i+1, nums[i])

    for _ in range(M + K):
        a, b, c = map(int, input().split())

        if a == 1:
            tree = update_fenwick_tree(tree, b, c - nums[b-1])
            nums[b-1] = c
        elif a == 2:
            print(query_fenwick_tree(tree, c) - query_fenwick_tree(tree, b-1))