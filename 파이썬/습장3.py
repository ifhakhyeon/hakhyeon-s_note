class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        if self.parent is not None:
            if self.parent.left.data == self.data:
                self.direction = left
            elif self.parent.right.data == self.data:
                self.direction = 'right'
        else:
            self.direction = None

node1 = Node(10)
node2 = Node(20)
node2.right = node1
node1.parent = node2

print(node1.parent.right.data)
print(node1.direction)