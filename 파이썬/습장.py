n = int(input())
inf = 9876543210
arr = []
height = {}
def lower_bound(nums, target):
    left, right = 0, len(nums)
    while left < right:  # left와 right가 만나는 지점이 target값 이상이 처음 나오는 위치
        mid = left + (right - left) // 2

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return right

ret = 0
for _ in range(n):
    n = int(input())
    k = lower_bound(arr, n)
    if k == 0 and arr == []:
        arr.append(n)
        height[n] = 1
        ret += 1
    elif k == 0 and arr != []:
        height[n] = height[arr[0]] + 1
        ret += height[arr[0]] + 1
        arr = [n] + arr
    elif k == len(arr):
        height[n] = height[arr[-1]] + 1
        ret += height[arr[-1]] + 1
        arr = arr + [n]
    else:
        height[n] = max(height[arr[k]], height[arr[k-1]]) + 1
        ret += max(height[arr[k]], height[arr[k-1]]) + 1
        arr.append(n)
        arr.sort()
print(ret)
# https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=occidere&logNo=221133866451