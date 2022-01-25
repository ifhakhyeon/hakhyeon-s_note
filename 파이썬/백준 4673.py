import sys

input = sys.stdin.readline

field = [0 for _ in range(10001)]


def notself(N):
    # sum은 계속 바뀌니까 따로 할당해줌
    sum = N
    while True:
        # N 에 sum을 10으로 나눈 나머지를 더함
        N += sum % 10
        # sum은 다시 자신을 10으로 나는 몫
        sum //=10
        # sum이 한자리 숫자면 마지막까지 다 나눈 거니까
        if sum <10:
            # 그 sum을 더해주고
            N += sum
            # while문 스탑
            break
    # 기저사례 N이 10000을 넘어가면 더이상 할 필요가 없음. 함수종료
    if N > 10000:
        return
    # 다른 두 수가 결국 다른 하나의 생성자가 되면 그 뒤에 결과는 같으므로 더 할필요 없음 함수종료
    if field[N] > 0:
        return
    # 위의 if 문을 통과하면 field 인댁스에 해당하는 숫자에 + 숫자가 +가 되면 그건 셀프넘버가 아님
    field[N] += 1
    # 바뀐 N으로 함수 제귀
    notself(N)

# 생성자가 여러개 있으므로 for문 전부탐색으로 풀 수 있었음 사실 아니여도 10000정도면 가능(100001은 불가능..)..
# 숫자가 0인 것들은 셀프넘버 즉 생성자가 없음
for i in range(10001):
    notself(i)

#이를 출력
for i in range(0, 10001):
    if field[i] == 0:
        print(i)

