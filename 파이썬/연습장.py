a = [-7, 4, -3, 6, 3, -8, 3, 4]

#동적 계획법! 파이썬 감각 살리기..
#
def fastestMaxSum(vector):
    N = len(vector) ; ret = -987645321 ; psum = 0

    for i in range(N):
        psum = max(psum,0) + vector[i]
        # 동작을 알기위한 테스트코드
        # print("psum :",psum, i)
        ret = max(psum, ret)
        # 동작을 알기위한 테스트코드
        # print("ret :",ret, i)

    return ret

print(fastestMaxSum(a))

#P. 119 설명 이해