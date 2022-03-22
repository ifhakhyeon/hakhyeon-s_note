_=input()
q=list(map(int,input().split()))
m,n=max(q),min(q)
a=[0]*(m-n+1)
for i in q:a[i-n]+=1
b=a[0]
for i in a[1:]:
    if b<=0:b=99
    else:b=i-b
print(1if b==0else-1)