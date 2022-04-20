import sys
input = sys.stdin.readline

N, K = map(int, input().split())
mod = 1000*1000*1000

cache = [[0] * (N+1) for _ in range(K+1)]
for i in range(N+1):
    cache[1][i] = 1
for i in range(1, K+1):
    cache[i][0] = 1

for k in range(2, K+1):
    for n in range(1, N+1):
        cache[k][n] += (cache[k-1][n] + cache[k][n-1])

print(cache[K][N] % mod)

'''
20을 5개로 나눈 것은 [0+(20을 4개로 나눈것)] + [1+(19를 4개로 나눈것)] + 
                                            ... + [19+(1을 4개로 나눈것)] + [20+(0을 4개로 나눈것)] 일 것이다.
즉 점화식으로 표현한다면, dp[n][k] = dp[0][k-1] + dp[1][k-1] + ... dp[n-1][k-1] + dp[n][k-1] 일 것이다.
그런데 이 점화식을 이용한다면 for문을 3개 이용해야 한다. 그래서 좀 더 간결화 할 수 있는 방법을 생각해보니,
dp[n-1][k] = dp[0][k-1] + dp[1][k-1] + ... dp[n-1][k-1] 임을 이용할 수 있겠다 생각이 싶었다.
따라서 dp[n][k] = dp[n-1][k] + dp[n][k-1] 으로 표현할 수 있다.

정답을 안찾아보고 풀고
그다음에 정확한 해설을 봤다.. 뭔가 찝찝하다.
'''