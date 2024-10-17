a,b=tuple(map(int,input().split()))
c=list(map(int,input().split()))
d=[]
for i in c:
    if i<b-1:
        d.append(i)
d.sort()
min=0
max=len(d)-1
now=0
try :
    while True:
        if min==max-1:
            break
        if d[min]+d[min+1]+d[min+2]<=b<=d[min]+d[max-1]+d[max]:
            for i in range(min+1,max):
                if d[min]+d[i]+d[i+1]<=b<=d[min]+d[max-1]+d[max]:
                    for j in range(i+1,max+1):
                        if now<d[min]+d[i]+d[j]<b:
                            now=d[min]+d[i]+d[j]
                        elif d[min]+d[i]+d[j]<=now:
                            continue
                        elif d[min]+d[i]+d[j]==b:
                            now=b
                            raise
                        elif d[min]+d[i]+d[j]>b:
                            break
                else:
                    break
            min=min+1
            continue
        elif d[min]+d[min+1]+d[min+2]>b:
            if now==0:
                break
            else:
                break
        elif d[min]+d[max-1]+d[max]<b:
            if now<d[min]+d[max-1]+d[max]:
                now=d[min]+d[max-1]+d[max]
                min=min+1
            else:
                min=min+1
except:
    pass
if now==0:
    pass
else:
    print(now)