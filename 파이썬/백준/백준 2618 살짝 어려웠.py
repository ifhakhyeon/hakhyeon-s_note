import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 애초에 case1, case2 로 지정하면서 cache가 좀 더 깔끔해졌다.
def go(a1, b1):
    if cache[a1][b1] != -1:
        return cache[a1][b1]
    if a1 == m or b1 == m:
        return 0
    idx = max(a1, b1) + 1

    dist_1 = abs(case1[a1][0] - case1[idx][0]) + abs(case1[a1][1] - case1[idx][1])
    dist_2 = abs(case2[b1][0] - case2[idx][0]) + abs(case2[b1][1] - case2[idx][1])

    result1 = dist_1 + go(idx, b1)
    result2 = dist_2 + go(a1, idx)

    cache[a1][b1] = min(result1, result2)
    return cache[a1][b1]

def pathPrint(a1, b1):
    if a1 == m or b1 == m:
        return
    idx = max(a1, b1) + 1

    dist_1 = abs(case1[a1][0] - case1[idx][0]) + abs(case1[a1][1] - case1[idx][1])
    dist_2 = abs(case2[b1][0] - case2[idx][0]) + abs(case2[b1][1] - case2[idx][1])

    result1 = dist_1 + cache[idx][b1]
    result2 = dist_2 + cache[a1][idx]

    if result1 < result2:
        print(1)
        pathPrint(idx, b1)
    else:
        print(2)
        pathPrint(a1, idx)

if __name__ == "__main__":
    n = int(input())
    m = int(input())

    cache = [[-1]*(m+2) for _ in range(m+2)]
    case1 = [(1, 1)]
    case2 = [(n, n)]
    for _ in range(m):
        case = tuple(map(int, input().split()))
        case1.append(case)
        case2.append(case)

    print(go(0, 0))
    # print(cache)
    pathPrint(0, 0)