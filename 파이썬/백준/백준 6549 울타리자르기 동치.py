import sys
input = sys.stdin.readline

def solve(left, right):
    # 기저사례 두개가 같으면 높이 반환
    if left == right:
        return hlist[left]
    # 가운대 이건 항상 정수
    mid = int((right+left)/2)
    # 왼쪽 오른쪽 나눠 생각함
    ret = max(solve(left, mid), solve(mid+1, right))
    lo = mid; hi = mid+1
    # 높이는 둘 중 낮은걸로
    height = min(hlist[lo], hlist[hi])
    ret = max(ret, height*2)
    # 사각형이 전체를 덮을 때까지 진행

    while(left < lo or hi < right):
        if hi < right and (lo == left or hlist[lo - 1] < hlist[hi + 1]):
            hi += 1
            height = min(height, hlist[hi])
        else:
            lo -= 1
            height = min(height, hlist[lo])

        ret = max(ret, height*(hi-lo+1))
    return ret

while True:
    h = input().strip()
    if h == '0':
        break
    else:
        h = list(map(int, h.split()))
    length = h[0]
    hlist = h[1:]
    print(solve(0, length-1))