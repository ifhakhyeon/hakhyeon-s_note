import sys
import math
input = sys.stdin.readline

def integral(arr, a, b, k=0):
    ret = [k]
    for i in range(len(arr)):
        ret.append(arr[i]*(1/(i+1)))

    return cal(ret, b) - cal(ret, a)

def cal(arr, x):
    ret = 0
    for i in range(len(arr)):
        ret += arr[i]*(x**i)
    return ret

def cal_fx(f, g):
    ret = [0] * (len(f)+len(g)-1)

    for i in range(len(f)):
        for j in range(len(g)):
            ret[i+j] += f[i]*g[j]

    return ret

x1, y1, x2, y2, x3, y3 = map(int, input().split())
def x_spine(x1, y1, x2, y2, x3, y3):
    a = [[x1, y1], [x2, y2], [x3, y3]]
    a.sort(key=lambda x: x[0])
    x1 = a[0][0]; y1 = a[0][1]; x2 = a[1][0]; y2 = a[1][1]; x3 = a[2][0]; y3 = a[2][1]
    if not (x1 == x2 or x2 == x3):
        d1 = (y1-y3)/(x1-x3); k1 = y1 - (d1 * x1)
        f1 = [k1, d1]
        d2 = (y1 - y2) / (x1 - x2); k2 = y1 - (d2 * x1)
        f2 = [k2, d2]
        d3 = (y2 - y3) / (x2 - x3); k3 = y2 - (d3 * x2)
        f3 = [k3, d3]
        return abs(integral(cal_fx(f1, f1), x1, x3) - integral(cal_fx(f2, f2), x1, x2) - integral(cal_fx(f3, f3), x2, x3)) * math.pi
    else:
        if x1 == x2:
            d1 = (y1 - y3) / (x1 - x3); k1 = y1 - (d1 * x1)
            f1 = [k1, d1]
            d3 = (y2 - y3) / (x2 - x3); k3 = y2 - (d3 * x2)
            f3 = [k3, d3]
            return abs(integral(cal_fx(f1, f1), x1, x3) - integral(cal_fx(f3, f3), x2, x3)) * math.pi
        elif x2 == x3:
            d1 = (y1 - y3) / (x1 - x3); k1 = y1 - (d1 * x1)
            f1 = [k1, d1]
            d2 = (y1 - y2) / (x1 - x2); k2 = y1 - (d2 * x1)
            f2 = [k2, d2]
            return abs(integral(cal_fx(f1, f1), x1, x3) - integral(cal_fx(f2, f2), x1, x2)) * math.pi

def y_spine(x1, y1, x2, y2, x3, y3):
    a = [[-y1, -x1], [-y2, -x2], [-y3, -x3]]
    a.sort(key=lambda x: x[0])
    x1 = a[0][0]; y1 = a[0][1]; x2 = a[1][0]; y2 = a[1][1]; x3 = a[2][0]; y3 = a[2][1]
    if not (x1 == x2 or x2 == x3):
        d1 = (y1-y3)/(x1-x3); k1 = y1 - (d1 * x1)
        f1 = [k1, d1]
        d2 = (y1 - y2) / (x1 - x2); k2 = y1 - (d2 * x1)
        f2 = [k2, d2]
        d3 = (y2 - y3) / (x2 - x3); k3 = y2 - (d3 * x2)
        f3 = [k3, d3]
        return abs(integral(cal_fx(f1, f1), x1, x3) - integral(cal_fx(f2, f2), x1, x2) - integral(cal_fx(f3, f3), x2, x3)) * math.pi
    else:
        if x1 == x2:
            d1 = (y1 - y3) / (x1 - x3); k1 = y1 - (d1 * x1)
            f1 = [k1, d1]
            d3 = (y2 - y3) / (x2 - x3); k3 = y2 - (d3 * x2)
            f3 = [k3, d3]
            return abs(integral(cal_fx(f1, f1), x1, x3) - integral(cal_fx(f3, f3), x2, x3)) * math.pi
        elif x2 == x3:
            d1 = (y1 - y3) / (x1 - x3); k1 = y1 - (d1 * x1)
            f1 = [k1, d1]
            d2 = (y1 - y2) / (x1 - x2); k2 = y1 - (d2 * x1)
            f2 = [k2, d2]
            return abs(integral(cal_fx(f1, f1), x1, x3) - integral(cal_fx(f2, f2), x1, x2)) * math.pi

print(x_spine(x1, y1, x2, y2, x3, y3), y_spine(x1, y1, x2, y2, x3, y3))