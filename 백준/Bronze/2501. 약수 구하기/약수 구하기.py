import math
받은숫자,몇번째=tuple(map(int,input().split()))
몇번째=몇번째-1
약수리스트=[]
진약수의합=0
for i in range(1,int(math.sqrt(받은숫자))+1):
    if 받은숫자%i==0:
        약수리스트.append(i)
    else:
        continue
half_list_개수=len(약수리스트)
for j in range(0,half_list_개수):
    약수리스트.append(받은숫자//약수리스트[j])
약수리스트=set(약수리스트)
약수리스트=list(약수리스트)
약수리스트.sort()
if 몇번째>=len(약수리스트):
    print(0)
else:
    print(약수리스트[몇번째])