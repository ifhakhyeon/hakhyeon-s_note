import queue164


class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
# numlist = TNode(0,1,2)
# print(numlist.right)
# print(numlist.data)
# print(numlist.left)

# 전위 순위 루트->왼->오
def preorder(n: TNode):
    if n is not None:
        print(n.data, end=' ')
        print(n.left)
        print(n.right)

# 중위 순위 왼->루트->오
def inorder(n: TNode):
    if n is not None:
        print(n.left)
        print(n.data, end=' ')
        print(n.right)

# 후위 순위 왼->오->루트
def postorder(n: TNode):
    if n is not None:
        print(n.left)
        print(n.right)
        print(n.data, end=' ')

# 레벨 순회
def levelorder(root: TNode):
    queue = queue164.CircularQueue() # 큐 객체 초기화
    queue.enqueue(root)              # 최초의 큐에는 루트노드만 들어있음
    while not queue.isEmpy():        # 큐가 공백 상태가 아닐 동안
        n = queue.dequeue()          # 큐에서 맨 앞의 노드 n을 꺼냄
        if n is not None:
            print(n.data, end=' ')   # 노드의 정보 먼저
            queue.enqueue(n.left)    # n의 왼쪽 자식 노드를 큐에 삽입
            queue.enqueue(n.right)   # n의 오른쪽 자식 노드를 큐에 삽입

# 노드 갯수 구하기
# 후위 순회의 방식 사용
def count_node(n: TNode):
    if n is None:                    # 공백이면 0 을 반환
        return 0
    else:                            # 좌우 서브트리의 노드수의 합 +1을 반환
        return 1+count_node(n.left) + count_node(n.right)

# 트리의 높이 구하기
def calc_height(n: TNode):
    if n in None:
        return 0
    hleft = calc_height(n.left)
    hright = calc_height(n.right)

    return max(hright, hleft) + 1



# class bstnode:
#     def __init__(self):(self, key, data):
#         self.key = key
#         self.data = data
#         self.left = None            # 왼쪽 자식에 대한 링크
#         self.right = None           # 오른쪽 자식에 대한 링크
#
#     # key == 루트의 키값 : 탐색 성공
#     # key < 루트의 키값 : 찾는 노드는 왼쪽 서브트리에 있음
#     # key > 루트의 키캆 : 찾는 노드는 오른쪽 서브트리에 있음

# 이건 key 값으로 value를 저장하기 때문에 value가 문자열이나 정수가 아닐때 유용한것 같다 다음은 프알문에 없는 구글링 이진탐색 트리를
# 적도록 하겠다..

# 노드 생성과 삽입

# 노드 생성과 삽입
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

    def dump(self):
        def print_subtree(node):
            # 전위 순회로 출력
            if node is not None:
                print(f'{node.data}')
                print_subtree(node.left)
                print_subtree(node.right)

        root = self.root
        print_subtree(root)