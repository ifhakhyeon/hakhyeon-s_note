import sys
input = sys.stdin.readline
n = int(input())

cache = list([[1] * 10])
# print(cache)
for _ in range(n):
    cache.append(list([0] * 10))

for i in range(1, n+1):
    for j in range(0, 10):
        for k in range(j+1):
            cache[i][j] += cache[i-1][k]

print(cache[n][9] % 10007)
'''

n / 끝의 수	0	1	2	3	4	~	9
        1	1	1	1	1	1	 	1
        2	1	2	3	4	5	 	10
        3	1	2	6	10	15	 	220
        
예를 들어 n=3 이고 끝의 수가 2인 수의 개수를 구하자면
n=2일 때 0, 1, 2의 개수를 모두 더한 수가 됩니다.
결국 만들 수 있는 모든 수는 끝의 수가 9인 경우를 구하면 문제에서 원하는 답이 도출됩니다.
'''
