import sys
input = sys.stdin.readline
import time

def solve(left, right):
    # 기저사례 두개가 같으면 높이 반환
    if left == right:
        return h[left]
    # 가운대 이건 항상 정수
    mid = int((right+left)/2)
    # 왼쪽 오른쪽 나눠 생각함
    ret = max(solve(left, mid), solve(mid+1, right))
    lo = mid; hi = mid+1
    # 높이는 둘 중 낮은걸로
    height = min(h[lo], h[hi])
    ret = max(ret, height*2)
    # 사각형이 전체를 덮을 때까지 진행
    while(left < lo or hi < right):
        if hi < right and (lo == left or h[lo-1] < h[hi+1]):
            hi += 1
            height = min(height, h[hi])
        else:
            lo -= 1
            height = min(height, h[lo])

        ret = max(ret, height*(hi-lo+1))
    return ret

C = int(input())
for _ in range(C):
    length = int(input())
    h = list(map(int, input().split()))
    start = time.time()
    print(solve(0, length-1))
    end = time.time()
    print(f"{end - start:.5f} sec")

# 이것도 시간초과.. pass
# https://oizys.tistory.com/notice/11
# https://careers.kakao.com/jobs/P-11842?part=TECHNOLOGY&keyword=%EB%8D%B0%EC%9D%B4%ED%84%B0&page=1
# http://www.aitimes.com/news/articleView.html?idxno=131977