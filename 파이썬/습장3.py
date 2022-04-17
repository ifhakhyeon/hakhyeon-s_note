import sys
import time
import datetime



input = sys.stdin.readline
INF = 9876543210
n = int(input())
start = time.time()
cache = [INF] * (n+1)
cache[1] = 1
for i in range(1, n+1):
    if int(i ** (1/2)) == i ** (1/2):
        cache[i] = 1
        continue
    for j in range(int(i ** (1/2)), 0, -1):
        cache[i] = min(cache[i], cache[j**2] + cache[i-j**2])
        if cache[i] == 2 or cache[i] == 1:
            break

print(cache[n])
end = time.time()
sec = (end - start)
result = datetime.timedelta(seconds=sec)
print(result)
# print(cache)