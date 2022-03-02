class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.count = 1

class splaytree():
    def __init__(self):
        self.root = None
    def find_grandp(self, node):
        if node is not None and node.parent is not None:
            return node.parent.parent
        else:
            return None
    # 바꾸려는게 부모의 왼쪽자식일때
    def rotate_left(self, node):
        c = node.right
        p = node.parent
        g = self.find_grandp(node)
        if g is not None:
            if g.left == p:
                g.left = node; node.parent = g
                node.right = p; p.parent = node
                p.left = c
                if c:
                    c.parent = p
            elif g.right == p:
                g.right = node; node.parent = g
                node.right = p; p.parent = node
                p.left = c
                if c:
                    c.parent = p
        elif g is None:
            node.right = p; p.parent = node
            p.left = c
            if c:
                c.parent = p
            self.root = node
            node.parent = None

    def rotate_right(self, node):
        c = node.left
        p = node.parent
        g = self.find_grandp(node)
        if g is not None:
            if g.left == p:
                g.left = node; node.parent = g
                node.left = p; p.parent = node
                p.right = c
                if c:
                    c.parent = p
            elif g.right == p:
                g.right = node; node.parent = g
                node.left = p; p.parent = node
                p.right = c
                if c:
                    c.parent = p
        elif g is None:
            node.left = p; p.parent = node
            p.right = c
            if c:
                c.parent = p
            self.root = node
            node.parent = None

    def splay(self, node):
        while True:
            if self.root == node:
                break
            elif self.find_grandp(node) is None:
                if node.parent and node.parent.left == node:
                    self.rotate_left(node)
                    break
                elif node.parent and node.parent.right == node:
                    self.rotate_right(node)
                    break
            elif self.find_grandp(node).left and self.find_grandp(node).left.left == node:
                self.rotate_left(node.parent)
                self.rotate_left(node)
            elif self.find_grandp(node).right and self.find_grandp(node).right.right == node:
                self.rotate_right(node.parent)
                self.rotate_right(node)
            else:
                if node.parent.left == node:
                    self.rotate_left(node)
                    self.rotate_right(node)
                elif node.parent.right == node:
                    self.rotate_right(node)
                    self.rotate_left(node)
    def insert(self, data):
        current_node = self.root
        if current_node is not None:
            while True:
                if data < current_node.data:
                    if current_node.left is not None:
                        current_node = current_node.left
                    else:
                        current_node.left = Node(data)
                        current_node.left.parent = current_node
                        self.splay(current_node.left)
                        break
                elif data > current_node.data:
                    if current_node.right is not None:
                        current_node = current_node.right
                    else:
                        current_node.right = Node(data)
                        current_node.right.parent = current_node
                        self.splay(current_node.right)
                        break
                elif data == current_node.data:
                    current_node.count += 1
                    self.splay(current_node)
                    break
        else:
            self.root = Node(data)
        return

    def search(self, data):
        current_node = self.root
        while current_node:
            if current_node.data == data:
                return True
            elif current_node.data > data:
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
            if current_node.data == data:
                is_search = True
                break
            elif data < current_node.data:
                parent = current_node
                current_node = current_node.left
            elif data > current_node.data:
                parent = current_node
                current_node = current_node.right

        if is_search is False:
            return False

        if current_node.count == 1:
            # 삭제할 노드가 자식 노드를 갖고 있지 않을 때
            if current_node.left is None and current_node.right is None:
                if data < parent.data:
                    parent.left = None
                elif data > parent.data:
                    parent.right = None
                # 이런경우 발생 x 부모가 먼저 찾아짐 그러면 즉 자식이 같은가 비교
                elif data == parent.data:
                    pass

            # 삭제할 노드가 자식 노드를 한 개 가지고 있을 때(왼쪽 자식 노드)
            if current_node.left is not None and current_node.right is None:
                if data < parent.data:
                    parent.left = current_node.left
                elif data > parent.data:
                    parent.right = current_node.left
                # 이런경우도 발생 x
                elif data == parent.data:
                    pass
            # 삭제할 노드가 자식 노드를 한 개 가지고 있을 때(오른쪽 자식 노드)
            if current_node.left is None and current_node.right is not None:
                if data < parent.data:
                    parent.left = current_node.right
                elif data > parent.data:
                    parent.right = current_node.right
                # 마찬가지로 발생 x
                elif data == parent.data:
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
                if data < parent.data:
                    parent.left = change_node
                    change_node.right = current_node.right
                    change_node.left = current_node.left
                elif data > parent.data:
                    parent.right = change_node
                    change_node.left = current_node.left
                    change_node.right = current_node.right

        elif current_node.count > 1:
            current_node.count -= 1

        return True

    def dump(self):
        def print_subtree(node):
            # 전위 순회로 출력
            if node is not None:
                c = node.count
                while c != 0:
                    print(f'{node.data}', end=' ')
                    c -= 1
                print('left')
                print_subtree(node.left)

                print('right')
                print_subtree(node.right)
        root = self.root
        print_subtree(root)

tree = splaytree()

# arr = list(map(int, input().split()))
arr = [50, 40, 30, 45, 20, 35, 44, 46, 10, 25]
# arr = [50, 40, 60]
for i in arr:
    tree.insert(i)
    print('---')
    tree.dump()
    print('---')
# print(tree.root.data)
# print(tree.root.right.right.data)
# tree.dump()
# print()
# tree.insert(30)
# tree.insert(26)
# tree.dump()
# print()
# tree.delete(30)
# tree.dump()