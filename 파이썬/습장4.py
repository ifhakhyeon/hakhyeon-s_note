import sys
input = sys.stdin.readline

left = [0]
right = [0]
N = int(input())

for _ in range(N):
    num = int(input())
    if len(left) == len(right):
        left.append(num)
        i = len(left) - 1
        while i != 1 and num < left[i // 2]:
            left[i] = left[i // 2]
            i //= 2
        left[i] = num
    else:
        if len(right) > 1 and left[1] < num:
            c = left[1]
            left[1] = num

            right.append(c)
            i = len(right) - 1
            while i != 1 and c < right[i // 2]:
                right[i] = right[i // 2]
                i //= 2
            right[i] = c
        else:
            right.append(num)
            i = len(right) - 1
            while i != 1 and num < right[i // 2]:
                right[i] = right[i // 2]
                i //= 2
            right[i] = num
    print(left[1])