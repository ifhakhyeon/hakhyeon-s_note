import sys
input = sys.stdin.readline


def inorder(root, level):
    global num
    if tree[root][0] != -1:
        inorder(tree[root][0], level + 1)
    row[level].append(num)
    # 중위 순회이므로 왼쪽이 하나 늘어날 때마다 오른쪽에 있는거 갯수 +1
    num += 1
    if tree[root][1] != -1:
        inorder(tree[root][1], level + 1)


n = int(input())
tree = [[0, 0] for _ in range(n + 1)]
node = [0 for _ in range(n + 1)]
row = [[] for _ in range(n + 1)]
num: int = 1

for i in range(n):
    root, left, right = map(int, input().split())
    tree[root][0] = left
    tree[root][1] = right

    # 루트노드를 찾기위한 count
    node[root] += 1
    if left != -1:
        node[left] += 1
    if right != -1:
        node[right] += 1

# 루트찾기
for i in range(1, n + 1):
    if node[i] == 1:
        root = i
        break

inorder(root, 1)
result = max(row[1]) - min(row[1]) + 1
level = 1
for i in range(2, n + 1):
    if row[i]:
        if result < max(row[i]) - min(row[i]) + 1:
            result = max(row[i]) - min(row[i]) + 1
            level = i

print(level, result)