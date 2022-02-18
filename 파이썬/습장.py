import sys
input = sys.stdin.readline
N = int(input())
meeting = []
for _ in range(N):
    a, b = map(int, input().split())
    meeting.append((a,b))
meeting.sort(key=lambda x : x[0])
meeting.sort(key=lambda x : x[1])



canmeeting = []
last = meeting[0]
canmeeting.append(last)

for j in range(1, N):
    if last[1] > meeting[j][0]:
        pass
    else:
        last = meeting[j]
        canmeeting.append(last)


print(len(canmeeting))