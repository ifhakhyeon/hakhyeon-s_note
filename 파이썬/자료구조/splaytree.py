# import sys
# sys.setrecursionlimit(10 ** 6)
class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.size = 0
        self.sum = 0

class splaytree():
    def __init__(self):
        self.root = None

    # noinspection PyMethodMayBeStatic
    def _find_grand_p(self, node):
        if node is not None and node.parent is not None:
            return node.parent.parent
        else:
            return None
    # 바꾸려는게 부모의 왼쪽자식일때

    def _rotate_left(self, node):
        c = node.right
        p = node.parent
        g = self._find_grand_p(node)
        # 할아버지가 None이면 parent == root 혹은 node == root <- 이 상황은 발생 x
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
        return

    def _rotate_right(self, node):
        c = node.left
        p = node.parent
        g = self._find_grand_p(node)
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
        return
    # 1. node가 루트이면 성공이므로 종료한다.
    # 2. node의 부모(p) node.parent가 루트이면 rotate(node)를 하고 종료한다(Zig Step)
    # 3. node의 조부모를 g라고 하면 다음 두 가지 경우가 있다.
    # 3-1. g->p의 방향과 p->node 의 방향이 같은 경우 rotate(p) 이후 rotate(node)를 행한다(Zig-Zig Step)
    # 3-2. g-p의 방향과 p->node의 방향이 다른 경우, rotate(node)를 두 번 행한다(Zig-Zag Step)
    # 4. 1로 돌아가서 루트가 될 때까지 반복한다.

    def _splay(self, node):
        while True:
            if self.root == node:
                # 이걸 적는 이유는 아래 2번째 elif 연산에 바로 root가 완성될 수 있음.
                break
            elif self._find_grand_p(node) is None:
                if node.parent and node.parent.left == node:
                    self._rotate_left(node)
                    break
                elif node.parent and node.parent.right == node:
                    self._rotate_right(node)
                    break
            elif self._find_grand_p(node).left and self._find_grand_p(node).left.left == node:
                self._rotate_left(node.parent)
                self._rotate_left(node)
            elif self._find_grand_p(node).right and self._find_grand_p(node).right.right == node:
                self._rotate_right(node.parent)
                self._rotate_right(node)
            else:
                if node.parent.left == node:
                    self._rotate_left(node)
                    self._rotate_right(node)
                elif node.parent.right == node:
                    self._rotate_right(node)
                    self._rotate_left(node)
        self.update()
        return

    def insert(self, key, data):
        current_node = self.root
        if current_node is not None:
            while True:
                if key < current_node.key:
                    if current_node.left is not None:
                        current_node = current_node.left
                    else:
                        current_node.left = Node(key, data)
                        current_node.left.parent = current_node
                        self._splay(current_node.left)
                        break
                elif key >= current_node.key:
                    if current_node.right is not None:
                        current_node = current_node.right
                    else:
                        current_node.right = Node(key, data)
                        current_node.right.parent = current_node
                        self._splay(current_node.right)
                        break
        else:
            self.root = Node(key, data)
        return

    def search(self, key):
        current_node = self.root
        while current_node:
            if current_node.key == key:
                return current_node.data
            elif current_node.key > key:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False
    # 위에랑 똑같은데 True 대신 Node 반환

    def _search_node(self, key):
        current_node = self.root
        while current_node:
            if current_node.key == key:
                return current_node
            elif current_node.key > key:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None

    def _part_maxnode(self, node):
        while node.right is not None:
            node = node.right
        return node

    def _part_minnode(self, node):
        while node.left is not None:
            node = node.left
        return node

    def delete(self, key) -> bool:
        is_search = False
        delete_node = self._search_node(key)
        self._splay(delete_node)
        if delete_node:
            # 양쪽 다 있음
            # 왼쪽 트리의 가장 큰 값을 splay 하고 그 노드 오른쪽에 원래 삭제할 노드의
            # 오른쪽 자식을 붙여줌
            if delete_node.right and delete_node.left:
                lt = delete_node.left
                rt = delete_node.right
                maxroot = self._part_maxnode(lt)
                lt = self.root
                lt.parent = None
                self._splay(maxroot)
                self.root.right = rt
                rt.parent = self.root
            # 오른쪽만 있음.
            elif delete_node.right and not delete_node.left:
                delete_node.right = self.root
                delete_node.right.parent = None
                is_search = True
            # 왼쪽만 있음.
            elif not delete_node.right and delete_node.left:
                delete_node.left = self.root
                delete_node.left.parent = None
                is_search = True
            else:
            # 다 없음.
                self.root = None
                is_search = True
        else:
            pass
        return is_search

    def _sub_count(self, node):
        node.size = 0
        if not node.left and not node.right:
            return node.size
        if node.left:
            node.left.size = self._sub_count(node.left)
            node.size += node.left.size + 1
        if node.right:
            node.right.size = self._sub_count(node.right)
            node.size += node.right.size + 1
        return node.size
    # def _sub_count(self, node):
    #     root = self.root
    #     nodelist = []
    #     nodelist.append(root)
    #     while True:
    #         if not nodelist:
    #             break
    #         current_node = nodelist[-1]
    #         current_node.size = None
    #         docount = False
    #
    #         if not current_node.right and not current_node.left:
    #             docount = True
    #
    #         if current_node.right:
    #             if current_node.right.size:
    #                 current_node.size += current_node.right.size
    #                 docount = True
    #             else:
    #                 docount = False
    #
    #         if current_node.left:
    #             if current_node.left.size:
    #                 current_node.size += current_node.left.size
    #                 docount = True
    #             else:
    #                 docount = False
    #
    #         if not docount:
    #             if current_node.right:
    #                 nodelist.append(current_node.right)
    #             if current_node.left:
    #                 nodelist.append(current_node.left)
    #
    #         elif docount:
    #             nodelist.pop()

    def _sub_sum(self, node):
        node.sum = node.data
        if not node.left and not node.right:
            return node.sum
        if node.left:
            node.left.sum = self._sub_sum(node.left)
            node.sum += node.left.sum
        if node.right:
            node.right.sum = self._sub_sum(node.right)
            node.sum += node.right.sum
        return node.sum

    def update(self):
        current_node = self.root
        self._sub_count(current_node)
        self._sub_sum(current_node)
        return
    # k번 째 값 찾기
    # k 는 1부터

    def find(self, k):
        current_root = self.root
        while True:
            # 첫번째는 가장 작은 노드를 찾으면 됨
            if k == 1:
                c = self._part_minnode(current_root)
                self._splay(c)
                return True
            # 왼자식이 존재하고 왼자식 +2 가 되는 이유는 왼자식과 자기자신 포함
            elif current_root.left and current_root.left.size + 2 == k:
                self._splay(current_root)
                return True
            elif current_root.left and current_root.left.size + 2 > k:
                current_root = current_root.left
            elif current_root.left and current_root.left.size + 2 < k:
                # 왼쪽을 빼줘야함 위의 조건에서 왼쪽은 존재함
                k -= (current_root.left.size + 2)
                current_root = current_root.right
            # 왼쪽이 없을 때 오른쪽으로 이동
            elif not current_root.left and current_root.right:
                k -= 1
                current_root = current_root.right
            # 왼쪽도 없고 오른쪽도 없으면 False 찾는 범위보다 큰 숫자입력한거임
            elif not current_root.left and not current_root.right:
                return False
    # 이거 오류 처리하기 end +1 , start -1 생각해보니 이건 구할때 임의의 노드2개를 넣으면 될듯

    def interval(self, start, end):
        self.find(end+1)
        root = self.root
        lt = self.root.left
        self.root = lt
        lt.parent = None
        self.find(start-1)
        root.left = self.root
        self.root.parent = root
        self.root = root
        return self.root.left.right.sum

    def dump(self):
        def print_subtree(node):
            # 전위 순회로 출력
            if node is not None:
                print(f'{node.key}', f'{node.data}', f'{node.size}', f'{node.sum}', end=' ')
                print('left')
                print_subtree(node.left)
                print('right')
                print_subtree(node.right)
        root = self.root
        print_subtree(root)

# input = sys.stdin.readline
# key = lambda x: x[1]
# sys.setrecursionlimit(10 ** 6)
# list = list(map(int, f.readline().split()))
# C = int(f.readline())

# INF = 9876543210
# # f = open(r"C:\Users\H30208\Desktop\조학현 공부노트\input.txt", 'r')
# # N, M, K = map(int, f.readline().split())
# N, M, K = map(int, input().split())
tree = splaytree()
# for i in range(N):
#     numlist.insert(i+1, int(input()))
#     # numlist.insert(i+1, int(f.readline()))
# numlist.insert(0, INF)
# numlist.insert(N+1, -INF)
# numlist.update()
# for _ in range(M + K):
#     # a, b, c = map(int, f.readline().split())
#     a, b, c = map(int, input().split())
#     if a == 1:
#         numlist.find(b+1)
#         numlist.update()
#         numlist.root.data = c
#     elif a == 2:
#         print(numlist.interval(b+1, c+1))
# numlist.dump()
# S = list(map(int, input().split()))
# S = [50, 40, 30, 45, 20, 35, 44, 46, 10, 25, 33, 34, 36, 37, 32, 31, 47]
arr = [50, 40, 30, 45, 20, 35, 44, 46, 10, 25]
# S = [10, 20, 25, 26(), 30, 35, 40, 44, 45, 46, 50]
# S = [50, 40, 60]
for i in arr:
    tree.insert(i, i)

# tree.dump()
# print()
tree.insert(20, 20)
tree.delete(20)
tree.delete(20)
# print(tree.interval(1, 4))
tree.dump()
# tree.delete(47)
# tree.dump()
# print()
# tree.delete(30)
# tree.dump()

# https://lsh424.tistory.com/73
# https://www.cs.usfca.edu/~galles/visualization/SplayTree.html
# https://cubelover.tistory.com/10
# https://seastar105.tistory.com/104
# https://aruz.tistory.com/180