import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

def pre_order(in_s, in_e, p_s, p_e):
    if in_s > in_e or p_s > p_e:
        return
    # postorder의 제일 마지막이 루트
    root = postorder[p_e]
    print(root, end=' ')
    # 루트의 idx
    root_idx = position[root]

    # 루트를 기준으로 왼쪽, 오른쪽 idx를 정함
    left = root_idx - in_s
    right = in_e - root_idx

    pre_order(in_s, in_s + left-1, p_s, p_s+left-1)
    pre_order(in_e-right+1, in_e, p_e-right, p_e-1)

# 위치 저장 .index 로 매번 찾는것 보다 빠름
position = [0] * (n+1)
for i in range(n):
    position[inorder[i]] = i
pre_order(0, n-1, 0, n-1)