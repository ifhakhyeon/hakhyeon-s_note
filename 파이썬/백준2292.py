n = int(input())

i=0

while True:
    if (n==1):
        print(1)
        break
    if ((3*i*(i+1))+1) >= (n):
        print(i+1)
        break
    else:
        i+=1


