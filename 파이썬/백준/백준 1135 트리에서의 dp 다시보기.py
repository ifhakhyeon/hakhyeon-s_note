import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
t = list(map(int, input().split()))

tree: list[list[int]] = [[] for _ in range(n+1)]
for i in range(1, n):
    tree[t[i]].append(i)

# cache[n] = n를 root로 하는 subtree에 정보를 모두 전달하는데 걸리는 시간
cache = [0] * n


def dp(n):
    child_tree = []
    for node in tree[n]:
        # Leaf까지 내려감
        dp(node)
        # 각 child를 root로 하는 subtree에 정보 전달하는데 걸리는 시간 모음
        child_tree.append(cache[node])
    if not tree[n]:
        # Child가 없으면 0
        child_tree.append(0)

    child_tree.sort(reverse=True)
    # 시간이 오래 걸리는 쪽부터 먼저 전화를 돌리기
    # 늦게 돌릴 수록 앞서 건 전화만큼의 시간 i 를 추가적으로 더해줘야 한다.
    need_time = [child_tree[i] + i + 1 for i in range(len(child_tree))]
    cache[n] = max(need_time)  # 그 중에 가장 오래 걸리는 시간을 저장


dp(0)
print(cache[0] - 1)      # Root node에 정보 전달하는 시간은 없으니 1빼기
