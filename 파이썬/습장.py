import sys
input = sys.stdin.readline


str = input().strip()
str = str.upper()

list = [0 for _ in range(ord("A"), ord("Z")+1)]
# print(list)
for i in str:
    list[ord(i)-ord("A")] += 1
max = (0,-1)
max_same = -1
for i in enumerate(list):
    if i[1] > max[1]:
        max = i
    elif i[1] == max[1]:
        max_same = max

if max == max_same:
    print("?")
else:
    print(chr(max[0]+ord("A")))