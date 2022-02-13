def minerror(start, end):
    large: int = (sumlist[end]-sumlist[start-1]) // (end-start+1)
    small: float = ((sumlist[end]-sumlist[start-1]) / (end-start+1))-((sumlist[end]-sumlist[start-1])//(end-start+1))
    if small >= 0.5:
        m = large+1
    else:
        m = large
    ret = qsumlist[end]-qsumlist[start-1]-2*m*(sumlist[end]-sumlist[start-1])+m*m*(end-start+1)
    return ret

def quantize(start, part):
    if start == L and part == 0:
        return 0
    if part == 0:
        return 987654312
    if cache[start][part] != -1:
        return cache[start][part]
    cache[start][part] = 987654321

    for size in range(1, L - start+1):
        cache[start][part] = min(cache[start][part],
                                 minerror(start, start + size - 1) + quantize(start + size, part - 1))
        # print(start, part, size)
        # for i in cache:
        #     print(i)
        # print('---------------')
    return cache[start][part]

C = int(input())
for _ in range(C):
    L, p = map(int, input().split())
    cache: list = [[-1 for _ in range(101)] for _ in range(11)]
    numlist: list = list(map(int, input().split()))
    numlist.sort()
    # 부분합
    sumlist = []; qsumlist = []
    sum: int = 0; qsum: int = 0
    for i in numlist:
        sum += i
        qsum += i*i
        sumlist.append(sum)
        qsumlist.append(qsum)
    # start = 0일 경우 기저사례
    sumlist.append(0); qsumlist.append(0)

    ret = quantize(0, p)

    print(ret)
    # print(sumlist)
    # print(qsumlist)
    # print(minerror(0, 0))
    # print(minerror(0, 1))
    # print(minerror(0, 2))
    # print(minerror(0, 3))