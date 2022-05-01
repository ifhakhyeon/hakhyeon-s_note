import sys
input = sys.stdin.readline

n = int(input())
numlist = list(map(int, input().split()))

numlist.sort()

ans = 1
for i in numlist:
    if ans < i:
        break
    ans += i

print(ans)
'''
생각해내는데 한참 걸렸다.
1 이라는 무게가 측정가능하고 k라는 무게추가 추가될 때
우리는 1, 1+k 무게가 측정가능하다.

1 2 3 까지 측정 가능하고 4가 들어오면 우리는
1 2 3 (4+0 1+4 2+4 3+4) 까지 측정이 가능하다.

다시말해 k까지 측정이 가능하고 k+1 의 측정 가능여부를 알고싶으면
다음 추의 무게가 k+1 초과만 아니면 우리는 그전에 측정 가능했던 무게를 고르고(0 포함)
그 위에 k만 올려놓으면 된다.

즉 다음에 들어올 무게 추가 측정가능 하고자하는 무게 이하인지만 확이하면 된다.
'''
# psum = [0] * n
# psum[0] = numlist[0]
# for i in range(1, n):
#     psum[i] += psum[i-1] + numlist[i]
#
#
# def bound(left, right, num):
#     # print('>', left, right, num)
#     while left <= right:
#         mid = (left + right) // 2
#         if psum[mid] < num:
#             left = mid + 1
#         elif psum[mid] > num:
#             right = mid - 1
#         else:
#             # print('return mid', mid)
#             return mid
#     # print('return right', mid)
#     return mid
#
#
# def check(right, num):
#     idx = bound(0, right, num)
#     # print(right, num, idx)
#     num -= numlist[idx]
#     if num < 0:
#         return False
#     elif num == 0:
#         return True
#     return check(idx, num)
