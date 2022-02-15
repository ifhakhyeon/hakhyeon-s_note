N = int(input())
list=[False for _ in range(-1000000,1000000+1)]
for _ in range(N):
    list[(int(input()))] = True
for i in range(1000000, 0, -1):
    if list[-i]:
        print(-i)
for i in range(0,1000000+1):
    if list[i]:
        print(i)

        # 갑자기 생각난 ㅈㄴ 이상한 알고리즘 ㅋㅋㅋㅋ..