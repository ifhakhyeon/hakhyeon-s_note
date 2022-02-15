# cache = [[0 for _ in range(100)] for _ in range(100)]
#
# A = list(map(int, input().split())) + [-9987654321]
# B = list(map(int, input().split())) + [-9987654321]
#
# def jlis(indexA, indexB):
#     if cache[indexA+1][indexB+1] != -1:
#         return cache[indexA+1][indexB+1]
#
#     ret = 2
