import sys
input = sys.stdin.readline
f = open(r"C:\Users\H30208\Desktop\조학현 공부노트\input.txt", 'r')
# C = int(input())
C = int(f.readline())
for _ in range(C):
    n, m = map(int, f.readline().split())
    # n, m = map(int, input().split())
    Qlist = list(map(int, f.readline().split()))
    # Qlist = list(map(int, input().split()))

    MAX_QSIZE = n+1

    class CircularQueue:
        def __init__(self):
            self.front = 0
            self.rear = n
            self.items = [0] + Qlist

        def isEmpy(self):
            return self.front == self.rear

        def isFull(self):
            return self.front == (self.rear+1) % MAX_QSIZE

        def clear(self):
            self.front = self.rear

        # rear 는 비어있지 않는 한 그곳에 뭔가가 있어..
        def enqueue(self, item):
            if not self.isFull():
                # 회전
                self.rear = (self.rear+1) % MAX_QSIZE
                # 회전한 곳에 아이템 저장
                self.items[self.rear] = item

            elif self.isFull():
                return -1

        # front 는 비어있든 뭐가됐든 그곳은 뭐가 없어..
        def dequeue(self):
            if not self.isEmpy():
                # 회전
                self.front = (self.front+1) % MAX_QSIZE
                # 회전된 곳의 아이템 반환
                return self.items[self.front]
            elif self.isEmpy():
                return -1

        def peek(self):
            if not self.isEmpy():
                return self.items[(self.front+1) % MAX_QSIZE]
            else:
                return -1

        def size(self):
            return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE

        def back(self):
            if not self.isEmpy():
                return self.items[self.rear]
            else:
                return -1

        def canprint(self):
            Qfront = self.peek()
            if self.size() != 1:
                if self.front < self.rear:
                    out = max(self.items[self.front + 1: self.rear + 1])
                else:
                    out = max(self.items[self.front + 1: MAX_QSIZE] \
                          + self.items[0:self.rear + 1])
                if Qfront >= out:
                    return True
                else:
                    return False
            else:
                return True

        def display(self):
            out = []
            if self.front < self.rear:
                out = self.items[self.front+1: self.rear+1]
            else:
                out = self.items[self.front+1: MAX_QSIZE]\
                +self.items[0:self.rear+1]
            print("[F=%s, r=%d] ==>"%(self.front, self.rear), out)

    count = 1
    where = m
    S = CircularQueue()
    # S.display()
    while True:
        print(where, end=' ')

        if where != 0:
            if S.canprint():
                count += 1
                S.dequeue()
                S.display()
            else:
                a = S.dequeue()
                S.enqueue(a)
                S.display()
            where -= 1

        elif where == 0:
            if S.canprint():
                print(count)
                break
            else:
                where = S.size()
                a = S.dequeue()
                S.enqueue(a)
                S.display()