from math import isqrt
import time
import datetime
from itertools import combinations_with_replacement as c
def e(n, b):
    v = 0
    while n > 1 and n % b == 0:
        n //= b
        v += 1
    return v
def o(n):
    return n // 4**e(n, 4) % 8

N = int(input())
start = time.time()
n = isqrt(N)

if n**2 == N:
    z = 1
elif o(N) == 7:
    z = 4
elif N in [sum(j) for j in c([i**2 for i in range(1, n+1)], 2)]:
    z = 2
else:
    z = 3
print(z)
end = time.time()
sec = (end - start)
result = datetime.timedelta(seconds=sec)
print(result)
