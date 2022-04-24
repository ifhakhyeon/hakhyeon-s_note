import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

bst = [-1] * 9876543210

while True:
# for _ in range(9):
    try:
        root = 1
        a = int(input())
        while bst[root] != -1:
            if bst[root] > a:
                root *= 2
                root += 1
            else:
                root *= 2
        bst[root] = a

    except ValueError:
        break

def dump():
    def print_subtree(node):
        if bst[node] != -1:
            print_subtree(node*2+1)
            print_subtree(node*2)
            print(bst[node])
    print_subtree(1)

dump()
