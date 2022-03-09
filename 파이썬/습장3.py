import sys
import math
from decimal import Decimal
input = sys.stdin.readline

A, B, C = map(float, input().split())

lo = ((C-B)/A)
hi = ((C+B)/B)

def sin(x):
    ret = 0
    for i in range(0, 200):
        a = Decimal(((-1) ** i) * (x ** (2*i+1)))
        a /= Decimal(math.factorial(2*i + 1))
        ret += a
    return ret

def fuc(x):
    return Decimal(A)*Decimal(x) + Decimal(B) * Decimal(sin(x))
mid = 1
for _ in range(100):
    mid = (Decimal(lo) + Decimal(hi)) / 2
    mid += Decimal(0.0000000000000000000000000000001)
    # print(mid)
    if fuc(mid) < C:
        lo = mid
    else:
        hi = mid

print(mid)
print(f'{mid:.6f}')

