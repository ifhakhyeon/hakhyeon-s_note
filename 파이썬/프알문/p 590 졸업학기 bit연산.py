import sys
input = sys.stdin.readline

INF = 9876543210
C = int(input())
for _ in range(C):
    n, k, m, l = map(int, input().split())
    pre = []

    for _ in range(n):
        a = list(map(int, input().split()))
        all = 0
        for i in range(a[0]):
            all |= (1 << a[i + 1])
        pre.append(all)
    classes = []

    for _ in range(m):
        a = list(map(int, input().split()))
        all = 0
        for i in range(a[0]):
            all |= (1 << a[i+1])
        classes.append(all)

    cache = [[-1] * (1 << n) for _ in range(m+1)]
    # print(pre, classes)
    def graduate(semester, taken):

        if bin(taken).count('1') >= k:
            return 0

        if semester == m:
            return INF

        # print(semester, taken, bin(taken))
        if cache[semester][taken] != -1:
            return cache[semester][taken]

        ret = INF
        cantaken = (classes[semester]) & (~taken)


        for i in range(n):
            # 1<<i 비트가 켜져있고       # 이미 선수강 경우 판단
            if cantaken & (1 << i) and taken & pre[i] != pre[i]:
                cantaken &= ~(1 << i)

        # 비트의 부분집합 순회하기!
        take = cantaken
        for i in range(cantaken):
            take = ((take-i) & cantaken)
        # 여기까지 꼭! 알아두기

            if bin(take).count('1') > l:
                continue
            ret = min(ret, graduate(semester+1, taken | take) + 1)

        ret = min(ret, graduate(semester+1, taken))

        cache[semester][taken] = ret

        return ret

    ans = graduate(1, 0)
    if ans != INF:
        print(ans)
    else:
        print('IMPOSSIBLE')
