import sys

class Node(object):
    def __init__(self, key, data=None):
        self.key = key              # key
        self.data = data            # flag 즉 문자열이 존재함을 나타냄
        self.children = {}          # 다음으로 이어지는 문자열

class Trie:
    def __init__(self):
        self.head = Node(None)      # head는 비어있음

    def insert(self, string):
        current_node = self.head

        for char in string:
            if char not in current_node.children:       # key로 시작하는 것이 없으면 생성
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]  # current node 갱신
        current_node.data = string                      # 삽입이 끝났으면 flag 세우기

    def search(self, string):
        current_node = self.head

        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]  # 있으면 이동
            else:
                return False                                # 없으면 false return

        if current_node.data:       # flag 확인
            return True
        else:
            return False

    def starts_with(self, prefix):
        current_node = self.head
        words = []

        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return None

        current_node = [current_node]
        next_node = []
        while True:
            for node in current_node:
                if node.data:
                    words.append(node.data)
                next_node.extend(list(node.children.values()))
            if len(next_node) != 0:
                current_node = next_node
                next_node = []
            else:
                break

        return words

    def search_prefix(self, prefix):
        current_node = self.head

        # print(prefix)
        for s in prefix:
            # print(s)
            try:
                current_node = current_node.children[s]
                if current_node.data and current_node.data != prefix:
                    # print('분기 1')
                    return True
            except KeyError:
                # print('분기 2')
                return False

        if current_node.children:
            # print('분기 3')
            return True
        else:
            # print('분기 4')
            return False

#
# input = sys.stdin.readline
# C = int(input())
# for _ in range(C):
#     n = int(input())
#     call_number = []
#     call_book = Trie()
#     for _ in range(n):
#         a = input().rstrip()
#         call_number.append(a)
#         call_book.insert(a)
#
#     ans = True
#     for number in call_number:
#         if call_book.search_prefix(number):
#             ans = False
#             break
#     if ans:
#         print('YES')
#     else:
#         print('NO')
#
