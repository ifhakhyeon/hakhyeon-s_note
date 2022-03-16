import sys
input = sys.stdin.readline

N, K = int(input()), int(input())
start = 1
end = N*N

while start <= end:
    mid = (start + end) // 2
    temp = 0
    for i in range(1, N + 1):
        temp += min(mid // i, N)  # mid 이하의 i의 배수 or 최대 N
    if temp >= K:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)