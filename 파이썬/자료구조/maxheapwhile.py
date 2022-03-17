import sys
input = sys.stdin.readline

heap = [0]
N = int(input())

def delete():
    parent = 1
    child = 2
    if len(heap) >= 2:
        hroot = heap[1]
        last = heap[len(heap) - 1]
        while child <= len(heap)-1:
            if child < len(heap)-1 and heap[parent * 2] > heap[parent * 2 + 1]:
                child += 1
            if last <= heap[child]:
                break
            heap[parent] = heap[child]
            parent = child
            child *= 2
        heap[parent] = last
        heap.pop(-1)
        return hroot
    else:
        return 0

for _ in range(N):
    num = int(input())
    if num == 0:
        print(delete())
    else:
        heap.append(num)
        i = len(heap) - 1
        while i != 1 and num < heap[i // 2]:
            heap[i] = heap[i // 2]
            i //= 2
        heap[i] = num
