import sys
input = sys.stdin.readline

class Node(object):
    def __init__(self, key, data=None):
        self.key = key              # key
        self.data = data            # flag 즉 문자열이 존재함을 나타냄
        self.children = {}          # 다음으로 이어지는 문자열

class Trie:
    def __init__(self):
        self.head = Node(None)      # head는 비어있음

    def insert(self, string_list):  # 입력을 list로 받음
        current_node = self.head

        for char in string_list:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]

    def dump(self, current_node, floor: int):
        # key 값으로 정렬 value는 Node이므로 정렬 불가
        current_node.children = dict(sorted(current_node.children.items(), key=lambda x: x[0]))
        # 층을 구별
        floor_str = '--' * floor
        for i in current_node.children:
            # 출력
            print(f'{floor_str}{i}')
            # 자기의 자식들 출력
            self.dump(current_node.children[i], floor + 1)

n = int(input())
ant = Trie()
for _ in range(n):
    a = list(input().split())
    ant.insert(a[1:])
ant.dump(ant.head, 0)