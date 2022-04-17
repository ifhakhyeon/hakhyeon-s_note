import sys
import time
import datetime

from math import isqrt
from itertools import combinations_with_replacement as c

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
# 내가 푼 일반적인 풀이다. 10,0000를 대입 했을 때 시간이
# 13.101976 초가 나온다. 느리다.

def e(n, b):
    v = 0
    while n > 1 and n % b == 0:
        n //= b
        v += 1
    return v
def o(n):
    return n // 4**e(n, 4) % 8

'''
여기서 e와 o는 르장드르 세 제곱수의 정리를 표현한거 같다.
n = 4^a (8b+7) 의 형태만 아니면 세제곱수의 함으로 표현 할 수 있다는 것이다.
'''

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

# 상당히 빠른 풀이다.
# 10,0000 이 00.006013 초가 나온다.
# 역시 배울건 많다.
# http://www.secmem.org/blog/2019/10/18/sum-of-squares/ 참고 링크