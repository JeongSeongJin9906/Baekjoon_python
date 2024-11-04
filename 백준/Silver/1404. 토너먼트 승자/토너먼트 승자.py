a=list(map(int,input().split()))
a=[(i/100) for i in a]
b=[(1-i) for i in a]
percent_ij=[[0]+a[int(i*(15-i)/2):int((i+1)*(14-i)/2)] for i in range(0,7)]+[[0]]
percent_ji=[[0]+b[int(i*(15-i)/2):int((i+1)*(14-i)/2)] for i in range(0,7)]+[[0]]
percent=[[]]
for j in range(1,8):
    list=[]
    for i in range(0,j):
        list.append(percent_ji[i][j-i])
    percent.append(list)
percent_total=[percent[i]+percent_ij[i] for i in range(0,8)]
def function(per_total,n):
    if n%2==0:
        return(per_total[n][n+1])
    else:
        return(per_total[n][n-1])
def function2(per_total,n):
    sum=0
    for i in range(0,8):
        if n//2==i//2:
            pass
        elif n//4==i//4:
            sum=sum+function(per_total,n)*function(per_total,i)*per_total[n][i]
        else:
            pass
    return(sum)
def function3(per_total,n):
    sum2=0
    for i in range(0,8):
        if n//4==i//4:
            pass
        else:
            sum2=sum2+function2(per_total,n)*function2(per_total,i)*per_total[n][i]
    return(sum2)
result=[]
for m in range(0,8):
    result.append(function3(percent_total,m))
print(*result)