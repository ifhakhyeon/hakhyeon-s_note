import sys
input = sys.stdin.readline

N = int(input())
numlist = list(map(int, input.split()))

max = None
min = None
ans = []
stack = []
for i in range(N-1, -1, -1):
    if numlist[i] == N-1:
        max = i
        min = i
        ans.append(-1)
        stack.append(numlist[i])
    elif numlist[i] >= numlist[max]:
        max = i
        min = i
        ans.append(-1)
        stack = []
        stack.append(numlist[i])
    elif numlist[min] <= numlist[i] < numlist[max]:
        for i in reversed(stack):
            if i > numlist[i]:
                ans.append(-1)
    elif numlist[i] < numlist[min]:
