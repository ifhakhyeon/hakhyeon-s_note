import sys

input = sys.stdin.readline


class Node(object):
    def __init__(self, key, data=None):
        self.key = key  # key
        self.data = data  # flag 즉 문자열이 존재함을 나타냄
        self.children = {}  # 다음으로 이어지는 문자열


class Trie:
    def __init__(self):
        self.head = Node(None)  # head는 비어있음

    def insert(self, string):
        current_node = self.head

        for char in string:
            if char not in current_node.children:  # key로 시작하는 것이 없으면 생성
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]  # current node 갱신
        current_node.data = string  # 삽입이 끝났으면 flag 세우기

    def search(self, string):
        current_node = self.head

        count = 1
        current_node = current_node.children[string[0]]
        string = string[1:]
        for idx, char in enumerate(string):
            if current_node.data or len(current_node.children) > 1:
                count += 1
            current_node = current_node.children[char]
        return count


while True:
    try:
        n = int(input())
        book = Trie()
        booklist = []
        ans = 0
        for _ in range(n):
            a = input().strip()
            book.insert(a)
            booklist.append(a)
        for i in booklist:
            r = book.search(i)
            ans += r
            # print(r, i)
        print(f'{ans / n:.2f}')
    except ValueError:
        break

# https://hooongs.tistory.com/311 이 풀이도 좋은듯