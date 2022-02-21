import queue164

class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

# a = TNode(0,1,2)
# print(a.right)
# print(a.data)
# print(a.left)

# 전위 순위 루트->왼->오
def preorder(n):
    if n is not None:
        print(n.data, end=' ')
        print(n.left)
        print(n.right)

# 중위 순위 왼->루트->오
def inorder(n):
    if n is not None:
        print(n.left)
        print(n.data, end=' ')
        print(n.right)

# 후위 순위 왼->오->루트
def postorder(n):
    if n is not None:
        print(n.left)
        print(n.right)
        print(n.data, end=' ')

# 레벨 순회
def levelorder(root):
    queue = queue164.CircularQueue() # 큐 객체 초기화
    queue.enqueue(root)              # 최초의 큐에는 루트노드만 들어있음
    while not queue.isEmpy():        # 큐가 공백 상태가 아닐 동안
        n = queue.dequeue()          # 큐에서 맨 앞의 노드 n을 꺼냄
        if n is not None:
            print(n.data, end=' ')   # 노드의 정보 먼저
            queue.enqueue(n.left)    # n의 왼쪽 자식 노드를 큐에 삽입
            queue.enqueue(n.right)   # n의 오른쪽 자식 노드를 큐에 삽입

# 노드 갯수 구하기
# 후위 순회의 방식 사용
def count_node(n):
    if n is None:                    # 공백이면 0 을 반환
        return 0
    else:                            # 좌우 서브트리의 노드수의 합 +1을 반환
        return 1+count_node(n.left) + count_node(n.right)

# 트리의 높이 구하기
def calc_height(n):
    if n in None:
        return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)

    return max(hRight, hLeft) +1

class MaxHeap:                                          # 최대 힙 클래스
    def __init__(self):                                 # 생성자
        self.heap = []                                  # 리스트 이용
        self.heap.append(0)                             # 0번 은 사용 안함

    def size(self): return len(self.heap) - 1           # 힙의 크기
    def isempty(self): return self.size() == 0          # 공백 검사
    def parent(self, i): return self.heap[i // 2]       # 부모노드 반환
    def left(self, i): return self.heap[i * 2]          # 왼쪽 자식 반환
    def right(self, i): return self.heap[i * 2 + 1]     # 오른쪽 자식 반환
    def display(self, msg = '힙 트리: '):
        print(msg, self.heap[1:])
    def insert(self, n):
        self.heap.append(n)                             # 맨 마지막 노드로 일단 삽입
        i = self.size()                                 # 노드 n의 위치
        while (i != 1 and n > self.parent(i)):          # 부모보다 큰 동안 계속 업힙
            self.heap[i] = self.parent(i)               # 부모를 끌어내림
            i //= 2                                     # i를 부모의 인덱스로 옮김
        self.heap[i] = n                                # 마지막 위치에 n 삽입

    def delete(self):
        parent = 1
        child = 2
        if not self.isempty():
            hroot = self.heap[1]                        # 삭제할 루트를 복사해둠
            last = self.heap[self.size()]               # 마지막 노드
            while (child <= self.size()):               # 마지막 노드 이전까지
                # 만약 오른쪽 노드가 더 크면 child를 1증가 (왼쪽은 기본노드)
                if child < self.size() and self.left(parent) < self.right(parent):
                    child += 1
                if last >= self.heap[child]:            # 더 큰 자식이 작으면
                    break                               # 삽입 위치를 찾음. down heap 종료
                self.heap[parent] = self.heap[child]    # 아니면 down heap 계속
                parent = child
                child  *= 2
            self.heap[parent] = last                    # 맨 마지막 노드를 parent 위치에 복사
            self.heap.pop(-1)                           # 맨 마지막 노드 삭제
            return hroot                                # 저장해두었던 루트 반환