import tree280 as t

array = [50, 40, 0, 45, -1, 1, 43, 46]

bst = t.BinarySearchTree()
for x in array:
    bst.insert(x)

print(bst.root.left.data)
if bst.root.left.left:
    print(bst.root.left.left.data)
    print('이게 왜 되노')
print(bst.root.left.right.data)
print(bst.root.left.right.right.data)
print(bst.root.left.left.data)

print(bst.find(43))
print(bst.find(46))
print(bst.find(0))
print(bst.find(-1))
print(bst.find(1))
print(bst.dump())