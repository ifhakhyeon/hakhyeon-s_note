from bisect import bisect_left

N = int(input())
S = [0] + list(map(int, input().split()))
cache = [0 for _ in range(N+1)]
lis = [-9876543210] # 이진탐색을 위해 생성.
maxVal = 0 #최대값을 저장할 변수

for i in range(1, N+1):
    if lis[-1] < S[i]: #이진탐색으로 저장된 값들은 정렬되므로 맨 뒤의 값 비교.
        lis.append(S[i])
        cache[i] = len(lis) - 1
        maxVal = cache[i]
    else:
        cache[i] = bisect_left(lis, S[i]) #현재 값이 어느 위치의 값에 해당하는지 비교.
        lis[cache[i]] = S[i] #lis 업데이트.
print(maxVal)

res = []
for i in range(N, 0, -1):
    if cache[i] == maxVal:
        res.append(S[i])
        maxVal -= 1
res.reverse()
print(*res)

# 내 생각에 알고리즘 만드는 사람들은 천재다.
# LIS에서 lis를 찾는 알고리즘이 몇개나 있는건지 모르겠다;;
# 나중에 다 모아서 한번 봐야겠다
# print(*arr) 가변인자를 알았다... 왜안쓰고 있었지..?