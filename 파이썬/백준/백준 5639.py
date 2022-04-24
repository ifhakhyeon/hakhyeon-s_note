import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

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
                else:
                    pass
        else:
            self.root = Node(data)
        return

    def dump(self):
        def print_subtree(node):
            if node is not None:
                print_subtree(node.left)
                print_subtree(node.right)
                print(node.data)
        root = self.root
        print_subtree(root)

bst = BinarySearchTree()

while True:
    try:
        bst.insert(int(input()))
    except ValueError:
        break
bst.dump()


