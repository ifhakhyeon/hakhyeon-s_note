import sys
input = sys.stdin.readline

N, M = map(int, input().split())

target = list(map(int, input().split()))
front = 1
end = N
ans = 0
for i in range(M):
    # 앞에 있는걸 뒤로 넘길 때 등호가 if 에 포함되는건
    # 뒤에있는 걸 앞으로 넘기면 목표를 또 앞으로 넘기는 1회가 더 포함되기 때문에
    if target[i] - front <= end - target[i]:
        # 이동 횟수
        go = target[i]-front
        ans += go
        # 크기가 줄었으니 -1
        end -= 1
        # 앞으로 움직일 것들의 위치를 update
        for j in range(i+1, M):
            # 3번째껄 빼는데 4번때 것 부터는 그냥 위치를 마이너스 해줌
            if target[j] > target[i]:
                # go + 1 인 이유는 최종적으로 맨 앞에 것도 빠지기 때문
                target[j] -= (go+front)
            else:
                # 이거는 손으로 해보는 것이 더 빠름 이해가
                target[j] = end - (go-target[j])
    else:
        # 앞으로 넘기는 횟수
        go = end - target[i]
        # 뒤로애걸 앞으로 옮기는 연산은 마지막 자신을 앞으로 보내는 연산이 있으므요 +1
        ans += (go + 1)
        for j in range(i+1, M):
            if target[j] < target[i]:
                # 9 번째껄 빼는데 7번째 껀 그냥 위치를 + 해줌
                target[j] += go
            else:
                # 이것도 손으로 해보는게 더 빠름 이해가
                target[j] -= target[i]
        end -= 1

print(ans)