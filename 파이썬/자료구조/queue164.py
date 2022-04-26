MAX_QSIZE = 200*100*100


class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items =[None] * MAX_QSIZE

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
            pass

    # front 는 비어있든 뭐가됐든 그곳은 뭐가 없어..
    def dequeue(self):
        if not self.isEmpy():
            # 회전
            self.front = (self.front+1) % MAX_QSIZE
            # 회전된 곳의 아이템 반환
            return self.items[self.front]
        elif self.isEmpy():
            pass

    def peek(self):
        if not self.isEmpy():
            return self.items[(self.front+1) % MAX_QSIZE]

    def size(self):
        return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE

    def display(self):
        out = []
        if self.front < self.rear:
            out = self.items[self.front+1: self.rear+1]
        else:
            out = self.items[self.front+1: MAX_QSIZE]\
            +self.items[0:self.rear+1]
        print("[F=%s, r=%d] ==>"%(self.front, self.rear), out)


class CircularDeque(CircularQueue):
    def __init__(self):
        super().__init__()

    def addRear(self, item):
        self.enqueue(item)

    def deleteFront(self):
        return self.dequeue()

    def getFront(self):
        return self.peek()

    def addFront(self, item):
        if not self.isFull():
            self.items[self.front] = item
            self.front = self.front-1
            if self.front < 0:
                self.front = MAX_QSIZE-1

    def deleteRear(self):
        if not self.isEmpy():
            item = self.items[self.rear]
            self.rear = self.rear-1
            if self.rear < 0:
                self.rear = MAX_QSIZE-1
            return item

    def getRear(self):
        return self.items[self.rear]

# dq = CircularDeque()
#
# for i in range(9):
#     if i%2 == 0:
#         dq.addRear(i)
#     else:
#         dq.addFront(i)
#
# dq.display()

