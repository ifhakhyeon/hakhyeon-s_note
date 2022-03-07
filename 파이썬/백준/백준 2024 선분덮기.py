import sys
input = sys.stdin.readline
# key=lambda x: x[1]
# sys.setrecursionlimit(10 ** 6)

f = open(r"C:\Users\H30208\Desktop\조학현 공부노트\input.txt", 'r')
N = int(f.readline())
# N = int(input())
line = []
while True:
    a, b = map(int, f.readline().split())
    # a, b = map(int, input().split())
    if a == b == 0:
        break
    # if a > b:
    #     a, b = b, a
    if b <= 0 or a > N or a == b:
        continue
    else:
        line.append((a, b))

line.sort(key=lambda x: x[0])
# print(line)
INF = 9876543210
count = 0
part_line = [0, 0]
part_greedy = 0
end = 0
# 일단 가능한 선분이 있어야함
if line:
    # 제일 먼저 시작점이 0보다 작거나 같아야함.
    if line[0][0] <= 0:
        for i in line:
            # 시작점이 이전 구간 끝점보다 큰경우는 덮기 불가
            if i[0] > part_line[1] and i[0] > end and i[0] > part_greedy:
                break
            # 시작점이 끝점보다 작을 때까지 가장 멀리 나가는 값 찾기
            if i[0] <= part_greedy:
                end = max(end, i[1])
            # 처음으로 시작점이 이전 끝점보다 큰 구간이 나옴. 이제 제일 끝을 정해줌.
            elif i[0] > part_greedy:
                # 처음 나온 더 큰 시작점이 이전구간의 가장 멀리가는 값보다 크면 안댐
                if i[0] <= end:
                    # 부분 구간의 끝점을 늘려주고
                    part_line[1] = end
                    # print(part_line)
                    # 끝점 갱신
                    part_greedy = end
                    # end값 초기화
                    count += 1
                    if end >= N:
                        break
                    end = 0
                    # 다시 멀리나가는 값 탐색
                    end = max(end, i[1])
                elif i[0] > end:
                    break
        if part_line[1] < N:
            part_line[1] = end
            # print(part_line)
            count += 1
    else:
        pass
else:
    pass

if part_line[1] >= N:
    print(count)
else:
    print(0)