# class DNode:
#     def __init__(self, elem, prev = None, next = None):
#         self.key = elem
#         self.prev = prev
#         self.next = next
#
# class doublelinkedlist:
#     def __init__(self):
#         self.front = None
#         self.rear = None
#
#     def size(self):
#         node = self.front
#         b = 0
#         while not node == None:
#             node = node.next
#             b += 1
#         return b
#
#     def display(self, msg = "doublelinkedlist"):
#         print(msg, end ='')
#         node = self.front
#         while not node == None:
#             print(node.key, end=' ')
#             node = node.next
#         print()
