import sys
input = sys.stdin.readline

n = int(input())
cache = [-1] * (n+1)

def dnf(width):
    if width % 2 == 1:
        return 0
    if width < 0:
        return 0
    if width == 0:
        return 1
    if cache[width] != -1:
        return cache[width]
    ret = 0
    ret += 3*dnf(width-2)
    for i in range(2, width//2 + 1):
        ret += 2*dnf(width-2*i)

    cache[width] = ret
    return ret

print(dnf(n))

'''
우선 n이 홀수일 경우 경우의 수는 0이다.
n = 2의 경우, 경우의 수는 3.
n = 4의 경우, 경우의 수는 11이다.
dp[2] * dp[2]에
새로운 모양 2개를 더해준다. 새로운 모양은 집모양 위아래 뒤집기이다
ㅡㅡ ㅡㅡ ㅡㅡ ㅡㅡ
ㅣ ㅡㅡ ㅡㅡ ㅡㅡ ㅣ
ㅣ ㅡㅡ ㅡㅡ ㅡㅡ ㅣ 다음과 같은 모양
n = 6의 경우, 경우의 수는 41이다.
dp[2] * dp[4]에 새로운 모양[4] * dp[2]를 더하고
새로운 모양 2개를 더해준다.
n = 8의 경우
경우의 수는 153.
dp[2] * dp[6]
+
새로운 모양[4] * dp[4]
+
새로운 모양[6] * dp[2]를 더하고
새로운 모양 2개를 더해준다.
'''

n = int(input())
dp = [0 for i in range(31)]
dp[2] = 3
for i in range(4, 31, 2):
    dp[i] = dp[2] * dp[i - 2]
    for j in range(4, i, 2):
        dp[i] += 2 * dp[i - j]
    dp[i] += 2
print(dp[n])