import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data) -> bool:
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node

    # 노드 탐색
    def find(self, key) -> bool:
        return self._find_value(self.root, key)

    def _find_value(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key <= root.data:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)

    def delete(self, key) -> bool:
        self.root, deleted = self._delete_value(self.root, key)
        return deleted

    def _delete_value(self, node, key):
        if node is None:
            return node, False

        deleted = False
        # 해당 노드가 삭제할 노드일 경우
        if key == node.data:
            deleted = True
            # 삭제할 노드가 자식이 두개일 경우
            # data가 아니고 그냥 노드 객체이므로 이 if 문은 성립
            if node.left and node.right:
                # 오른쪽 서브 트리에서 가장 왼쪽에 있는 노드를 찾고 교체
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            # 자식 노드가 하나일 경우 해당 노드와 교체
            elif node.left or node.right:
                node = node.left or node.right
            # 자식 노드가 없을 경우 그냥 삭제
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self._delete_value(node.left, key)
        else:
            node.right, deleted = self._delete_value(node.right, key)
        return node, deleted

    def minnode(self) -> int:
        node = self.root
        while node.left is not None:
            node = node.left
        return node.data

    def maxnode(self) -> int:
        node = self.root
        while node.right is not None:
            node = node.right
        return node.data

    #least minus num
    def findlmn(self, num) -> int:
        node = self.root

        if node is None:
            return -1

        while True:
            if node.data == num:
                return node.data

            elif node.data > num:               # 현제 노드 값이 비교하는 값보다 크고
                if node.left is not None:       # 왼쪽 자식이 None이 아니고
                    if node.left.data >= num:   # 왼쪽 자식이 비교하는 값보다 크면
                        node = node.left        # 노드 체인지

                    elif node.left.data < num:  # 왼쪽 작식이 더 작으면
                        return node.data        # 현제 노드 반환

                elif node.left is None:         # 왼쪽이 None이면 현제 노드 반환
                    return node.data

            elif node.data < num:
                if node.right is not None:     # 현제 노드가 비교한는 값보다 작으면
                    node = node.right          # 더 큰값 찾으로 오른쪽 자식으로
                elif node.right is None:
                    return self.minnode()      # 만약 오른쪽이 None이면 비교한느 값보다 큰값 없음

C = int(input())
for _ in range(C):
    n = int(input())
    russia = list(map(int, input().split()))
    korea = list(map(int, input().split()))
    skorea = BinarySearchTree()

    for i in korea:
        skorea.insert(i)
    # print(skorea.minnode())

    wins = 0
    for i in russia:
        who = skorea.findlmn(i)
        # print(who)
        if i <= who:
            wins += 1
            skorea.delete(who)
        else:
            skorea.delete(who)
    print(wins)

#https://algospot.com/judge/problem/read/MATCHORDER