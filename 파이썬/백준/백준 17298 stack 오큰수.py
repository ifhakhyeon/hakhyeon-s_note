import sys

input = sys.stdin.readline

N = int(input())
numlist = list(map(int, input().split()))
ans = []
stack = []
for i in reversed(numlist):
    # 스택이 비었으면 오큰수는 없음
    if not stack:
        # -1 추가
        ans.append(-1)
        stack.append(i)
    else:
        # 스택이 비지 않았으면 오큰수를 찾기위해 스택을 pop하면서 검사
        while True:
            # pop 하다가 스택이 비면 -1추가 하고 자기자신 추가
            # 여태까지의 수가 다 자기자신보다 작은거임
            if not stack:
                ans.append(-1)
                stack.append(i)
                break
                # 스택의 최근 수가 더 크면 답에 추가하고 자기자신 추가
            elif stack[-1] > i:
                ans.append(stack[-1])
                stack.append(i)
                break
                # 스택의 최근 수가 더 작으면 pop
            elif stack[-1] <= i:
                stack.pop()

for i in reversed(ans):
    print(i, end=' ')
