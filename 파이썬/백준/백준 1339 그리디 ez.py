import sys
n = int(input())
ll = [0 for i in range(ord('A'), ord('Z')+1)]

for _ in range(n):
    a = input().strip()
    k = len(a)
    for i in range(k):
        # print(ord(a[k-i-1]))
        ll[ord(a[k-i-1]) - ord('A')] += 10**i

ll.sort(reverse=True)
# print(ll)
ans = 0
m = 9
for i in range(10):
    ans += ll[i]*m
    m -= 1
print(ans)


