number=int(input())
m=number//5
s=number-m*5
if s==4:
    if m-1<0:
        print(-1)
    else:
        print(m+2)
elif s==3:
    print(m+1)
elif s==2:
    if m-2<0:
        print(-1)
    else:
        print(m+2)
elif s==1:
    if m-1<0:
        print(-1)
    else:
        print(m+1)
else:
    print(m)
