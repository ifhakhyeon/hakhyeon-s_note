# class DNode:
#     def __init__(self, elem, prev = None, next = None):
#         self.data = elem
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
#         count = 0
#         while not node == None:
#             node = node.next
#             count += 1
#         return count
#
#     def display(self, msg = "doublelinkedlist"):
#         print(msg, end ='')
#         node = self.front
#         while not node == None:
#             print(node.data, end=' ')
#             node = node.next
#         print()
