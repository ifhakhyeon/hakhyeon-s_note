import sys
input = sys.stdin.readline

N = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))
# 마지막껀 왜있누?
cost.pop(-1)
ans = 0
nowcost = 9876543210
godistance = 0
for i in range(N-1):
    if nowcost == min(nowcost, cost[i]):
        godistance += distance[i]
    elif nowcost != min(nowcost, cost[i]):
        ans += (godistance * nowcost)
        godistance = distance[i]
        nowcost = min(nowcost, cost[i])
ans += (godistance * nowcost)
print(ans)