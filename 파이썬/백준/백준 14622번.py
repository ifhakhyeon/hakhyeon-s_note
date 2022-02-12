def least(num):
    return int(num ** (1 / 2))
# 점수 계산
def point(cache):
    if len(cache) < 3:
        ret = 1000
    else:
        ret = min(cache)
    return ret

list = [True for _ in range(5000000 + 1)]
listcache = [False for _ in range(5000000 + 1)]
# 기저 사례 0과 1은 소수가 아님
list[0] = False ; list[1] = False
Maxcall = 5000000
least_N = least(Maxcall)
# 체
for i in range(2, least_N + 1):
    if list[i] >= 1:
        for j in range(2 * i, Maxcall+1, i):
            list[j] = False
# 부른 숫자 3개 기록
cacheD = []
cacheG = []
# 각자의 점수
Dscore = 0
Gscore = 0

C = int(input())
for k in range(C):
    Daewoong, Gueseong = map(int, input().split())

    # 대웅이부터 숫자를 부르는 걸로 함
    # 대웅이 소수를 부름
    if list[Daewoong] == True:
        # 부를 소수가 안불린 숫자라면
        if listcache[Daewoong] == False:
            if len(cacheD) < 3:
                cacheD.append(Daewoong)
            else:
                cacheD.append(Daewoong)
                # 가장 작은거 아웃!
                cacheD.remove(min(cacheD))
            # 그 소수는 불린것으로 바꿈
            listcache[Daewoong] = True
        else:
            # 불린 숫자라면 -1000 점
            Dscore -= 1000
    else:
        # 대웅이가 먼저 부르므로 대웅이가 소수가 아닌 숫자를 불렀을 때는
        # 입력받은 규성이의 숫자는 아직 안불린 상태여야함. 와 씨방 이거때문에 개고생했네
        Gscore += point(cacheG)

    # 이하 동문 같은 코드형식
    if list[Gueseong] == True:
        if listcache[Gueseong] == False:
            if len(cacheG) < 3:
                cacheG.append(Gueseong)
            else:
                cacheG.append(Gueseong)
                cacheG.remove(min(cacheG))
            listcache[Gueseong] = True
        else:
            Gscore -= 1000
    else:
        Dscore += point(cacheD)
    # print('k',k,Dscore, Gscore)

if Dscore == Gscore:
    print('우열을 가릴 수 없음')
elif Dscore > Gscore:
    print('소수의 신 갓대웅')
else:
    print('소수 마스터 갓규성')
# print(Dscore, Gscore)
# print(cacheD, cacheG)