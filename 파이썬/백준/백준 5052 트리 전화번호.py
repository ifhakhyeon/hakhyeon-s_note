import sys

input = sys.stdin.readline


class Node():
    def __init__(self):
        self.next = [None for _ in range(10)]
        self.complete = False

C = int(input())
for _ in range(C):
    tree = [None for _ in range(10)]

    n = int(input())
    can = True

    for _ in range(n):
        if not can:
            input()
            continue
        else:
            num = input().strip()
            length = len(num)
            s: int = int(num[0])

            if length == 1 and tree[s]:
                now = tree[s]
                can = False
                now.complete = True

            elif length == 1 and not tree[s]:
                tree[s] = Node()
                now = tree[s]
                now.complete = True


            elif not tree[s]:
                tree[s] = Node()
                now = tree[s]

            else:
                now = tree[s]
                if now.complete:
                    can = False
                    continue

            for i in range(1, length):

                k = int(num[i])

                if not now.next[k]:
                    now.next[k] = Node()
                    now = now.next[k]
                    if i == length - 1:
                        now.complete = True

                else:
                    if i == length - 1:
                        now.next[k].complete = True
                        can = False
                        break

                    elif now.next[k].complete:
                        can = False
                        break

                    else:
                        now = now.next[k]

    print('YES' if can else 'NO')

# 확실히 정렬하고 이래하는게 더 좋은듯
t = int(input())
def find(phonebook):
    for i in range(len(phonebook)-1):
        if phonebook[i] == phonebook[i+1][0:len(phonebook[i])]:
            return "NO"

for _ in range(t):
    n = int(input())
    tree = []
    for _ in range(n):
        number = input()
        tree.append(number.rstrip())
    tree.sort()
    answer = find(tree)
    if answer == None:
        answer = "YES"
    print(answer)

'''
trie 모듈 import 하면 정답임
input = sys.stdin.readline
C = int(input())
for _ in range(C):
    n = int(input())
    call_number = []
    call_book = Trie()
    for _ in range(n):
        a = input().rstrip()
        call_number.append(a)
        call_book.insert(a)

    ans = True
    for number in call_number:
        if call_book.search_prefix(number):
            ans = False
            break
'''
