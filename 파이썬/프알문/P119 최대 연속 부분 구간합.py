a = [-7, 4, -3, 6, 3, -8, 3, 4]

#동적 계획법! 파이썬 감각 살리기..
#부분합의 최댓값 구하기
def fastestMaxSum(vector):
    N = len(vector) ; ret = -987645321 ; psum = 0

    for i in range(N):
        psum = max(psum,0) + vector[i]
        # 동작을 알기위한 테스트코드
        # print("psum :",psum, i)
        ret = max(psum, ret)
        # 동작을 알기위한 테스트코드
        # print("p :",p, i)
# print(fastestMaxSum(q))

#P. 119 설명 이해
#인덱스를 반환하기 위해서는 후처리를 해야하구나..