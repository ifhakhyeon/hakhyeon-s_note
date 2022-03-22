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

a = [1, 2]
b = [2, 3]
print(cal_fx(a, b))
