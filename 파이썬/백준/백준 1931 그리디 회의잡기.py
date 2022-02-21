import sys
input = sys.stdin.readline
N = int(input())
meeting = []
for _ in range(N):
    a, b = map(int, input().split())
    meeting.append((a,b))
# 하 아니 이생각을 못해서 진짜 개고생 했다.. 왜 이리 단순하냐..
# 조금만 더 생각해보자 학현아.
meeting.sort(key=lambda x : x[0]) # 너 너한줄 추가하는걸 개고생했다..
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