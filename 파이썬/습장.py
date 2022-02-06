C = int(input())
for _ in range(C):
    a, b, c = map(int, input().split())
    if c//a == 0:
        front = str(c)
        back = '01'
    else:
        front = str(c % a)
    if c//a < 10:
        if a != 1:
            back = '0'+str((c//a)+1)
        else:
            back = f'0{c}'
    else:
        back = str((c//a)+1)

    print(front+back)