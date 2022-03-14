import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.count = 1
class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        current_node = self.root

        if current_node is not None:
            while True:
                if data < current_node.data:
                    if current_node.left is not None:
                        current_node = current_node.left
                    else:
                        current_node.left = Node(data)
                        break
                elif data > current_node.data:
                    if current_node.right is not None:
                        current_node = current_node.right
                    else:
                        current_node.right = Node(data)
                        break
                # 이미 삽입하려는 값이 있으면 왼쪽에 노드 하나를 추가하고 연결 시켜줌
                elif data == current_node.data:
                    # link = current_node.left
                    # current_node.left = Node(key)      # 새로운 노드랑 현재위치의 왼쪽자식과 연결
                    # current_node.left.left = link                    # 현재위치의 노드와 새로운 노드 연결
                    # 30의 자식이 두개 존재 실패임.
                    current_node.count += 1
                    break

        else:
            self.root = Node(data)
        return


    def search(self, data):
        current_node = self.root
        while current_node:
            if current_node.key == data:
                return True
            elif current_node.key > data:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False

    def delete(self, data):
        # 삭제할 노드가 있는지 검사하고 없으면 False리턴
        # 검사를 한 후에는 삭제할 노드가 current_node, 삭제할 노드의 부모 노드가 parent가 된다.
        is_search = False
        current_node = self.root
        parent = self.root
        while current_node:
            if current_node.key == data:
                is_search = True
                break
            elif data < current_node.key:
                parent = current_node
                current_node = current_node.left
            elif data > current_node.key:
                parent = current_node
                current_node = current_node.right

        if is_search is False:
            return False

        if current_node.b == 1:
            # 삭제할 노드가 자식 노드를 갖고 있지 않을 때
            if current_node.left is None and current_node.right is None:
                if data < parent.key:
                    parent.left = None
                elif data > parent.key:
                    parent.right = None
                # 이런경우 발생 x 부모가 먼저 찾아짐 그러면 즉 자식이 같은가 비교
                elif data == parent.key:
                    pass

            # 삭제할 노드가 자식 노드를 한 개 가지고 있을 때(왼쪽 자식 노드)
            if current_node.left is not None and current_node.right is None:
                if data < parent.key:
                    parent.left = current_node.left
                elif data > parent.key:
                    parent.right = current_node.left
                # 이런경우도 발생 x
                elif data == parent.key:
                    pass
            # 삭제할 노드가 자식 노드를 한 개 가지고 있을 때(오른쪽 자식 노드)
            if current_node.left is None and current_node.right is not None:
                if data < parent.key:
                    parent.left = current_node.right
                elif data > parent.key:
                    parent.right = current_node.right
                # 마찬가지로 발생 x
                elif data == parent.key:
                    pass

            # 삭제할 노드가 자식 노드를 두 개 가지고 있을 때
            if current_node.left is not None and current_node.right is not None:
                change_node = current_node.right
                change_node_parent = current_node.right
                # 삭제할 노드보다 큰갑중에(오른쪽 자식) 제일 작은값 구하기 그것이 바꿀 노드
                while change_node.left is not None:
                    change_node_parent = change_node
                    change_node = change_node.left

                # 바꿀 노드의 오른쪽의 값이 있으면 바꿀값의 부모와 연결
                if change_node.right is not None:
                    change_node_parent.left = change_node.right
                else:
                    change_node_parent.left = None
                # 삭제할 부모 노드의 데이터 가 부모보다 클때/작을 때
                if data < parent.key:
                    parent.left = change_node
                    change_node.right = current_node.right
                    change_node.left = current_node.left
                elif data > parent.key:
                    parent.right = change_node
                    change_node.left = current_node.left
                    change_node.right = current_node.right

        elif current_node.b > 1:
            current_node.b -= 1

        return True

    def minnode(self) -> int:
        node = self.root
        while node.left is not None:
            node = node.left
        return node.key

    def maxnode(self) -> int:
        node = self.root
        while node.right is not None:
            node = node.right
        return node.key

    def dump(self):
        def print_subtree(node):
            # 전위 순회로 출력
            if node is not None:
                c = node.b
                while c != 0:
                    print(f'{node.key}', end=' ')
                    c -= 1
                print('left')
                print_subtree(node.left)
                print('right')
                print_subtree(node.right)
        root = self.root
        print_subtree(root)

    # least minus num
    def findlmn(self, num) -> int:
        node = self.root

        if node is None:
            return -1

        while True:
            if node.key == num:
                return node.key

            elif node.key > num:  # 현제 노드 값이 비교하는 값보다 크고
                if node.left is not None:  # 왼쪽 자식이 None이 아니고
                    if node.left.key >= num:  # 왼쪽 자식이 비교하는 값보다 크면
                        node = node.left  # 노드 체인지

                    elif node.left.key < num:  # 왼쪽 작식이 더 작으면
                        return node.key  # 현제 노드 반환

                elif node.left is None:  # 왼쪽이 None이면 현제 노드 반환
                    return node.key

            elif node.key < num:
                if node.right is not None:  # 현제 노드가 비교하는 값보다 작으면
                    node = node.right  # 더 큰값 찾으로 오른쪽 자식으로
                elif node.right is None:
                    return self.minnode()  # 만약 오른쪽이 None이면 비교한느 값보다 큰값 없음


tree = BinarySearchTree()

# arr = list(map(int, input().split()))
# arr = [50, 40, 30, 45, 20, 35, 44, 46, 10, 25]
arr = [40, 50]
for i in arr:
    tree.insert(i)
    tree.dump()
# print()
# tree.insert(30)
# tree.insert(26)
# tree.dump()
# print()
# tree.delete(30)
# tree.dump()
