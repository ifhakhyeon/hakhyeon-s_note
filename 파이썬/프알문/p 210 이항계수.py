list = [[-1 for _ in range(10000)] for _ in range(10000)]
def bino(n, r):
    if r == 0 or r == n:
        return 1
    if list[n][r] != -1:
        return list[n][r]
    list[n][r] = bino(n - 1, r - 1) + bino(n - 1, r)
    return list[n][r]

print(bino(100, 50))

# 메모이제이션 구현 패턴




# 항상 기저사례를 제일 먼저 처리한다. 이때 입력값이 범위를 벗어난 경우도 생각한다.
# 반환값이 모두 0보다 크면 cache를 -1으로 초기화 한다 음수도 나오면 이건 무쓸모..
# 참조형 을 더 공부해보자
# import copy
# q = [[1], [2], [3]]
# p = copy.copy(q)
# print(hex(id(q)), hex(id(p)))
# p[0][0] = ['aa']
# p[1][0] = 'q'
# print(q, p)
# print(hex(id(q)), hex(id(p)))
# 뭔가 잘하면 써먹을 지도?
