import sys
input = sys.stdin.readline

cache = [-1 for _ in range(1000001)]
def soo(length):
    # 길이가 0 이거나 1이면 1가지 경우의 수만 나오기 때문에 1을 반환
    if length == 0 or length == 1:
        return 1
    # 길이가 음수인 경우 0 그건 있을 수 없음 근데 이건 없어도 될듯
    if length < 0:
        return 0

    if cache[length] != -1:
        return cache[length]

    cache[length] = 0
    # 짝수이면 반을 나누고 [반][반] 두개의 경우의 수를 곱하거나 [반-1][00][반-1] 이경우 두개임
    if length % 2 == 0:
        cache[length] = ((soo(length//2) * soo(length//2)) % 15746 + (soo((length//2)-1)**2) % 15746) % 15746
    # 홀수이면 [반][1][반] 이거나 [반-1][00]반 혹은 [반][00][반-1] 임 두번째 새번째는 경우의 수가 같으므로 *2 함
    elif length % 2 == 1:
        cache[length] = ((soo(length//2)**2) % 15746 + (2 * soo(length//2) * soo((length//2)-1)) % 15746) % 15746
    # 정수론 기본상식 덧샘의 나머지는 나머지+나머지를 다시 나눈것의 나머지임

    # 이건 초반에 실패했던 알고리즘
    # 나중에 절반으로 나눈 아이디어로 문제의 수를 반씩 줄여나감
    # cache[b] = ((soo(b-2) % 15746) + (soo(b - 1) % 15746)) % 15746

    return cache[length]

N = int(input())

print(soo(N))

# def soo2(b):
