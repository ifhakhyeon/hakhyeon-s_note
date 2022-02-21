import sys
input = sys.stdin.readline

def fprint(A):
    print('[', end='')
    for i in range(len(A)):
        print(A[i],end='')
        if i != len(A)-1:
            print(',',end='')
    print(']')

def count(do, A, front, end):
    reverse = 0
    for i in do:
        if i == 'R':
            reverse += 1
        elif reverse % 2 == 0 and i == 'D':
            front += 1
        elif reverse % 2 == 1 and i == 'D':
            end -= 1

    if front > end:
        print('error')
        return
    else:
        A = A[front:end]

    if reverse % 2 == 0:
        fprint(A)
        return
    elif reverse % 2 == 1:
        A.reverse()
        fprint(A)
        return



C = int(input())
for _ in range(C):
    do = input().strip()
    n = int(input())
    A = input().strip()
    # A = A[1:2*n] 으로 했다가 망함 왜냐하면 수가 한자리 수가아닌 두자리 수도 나올 수 있어서
    A = A[1:len(A)-1]
    if A != '':
        A = list(map(int, A.split(',')))
    else:
        A = []
    front = 0
    end = n
    count(do, A, front, end)

