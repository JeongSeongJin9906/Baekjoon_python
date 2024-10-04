몇번째=int(input())
n=1
while True:
    if (n**2)/2-(n/2)<몇번째<=(n**2)/2+(n/2):
        break
    else:
         n=n+1
몇칸=((n**2)/2+(n/2))-몇번째
if n%2==1:
    분모=n-몇칸
    분자=1+몇칸
else:
    분자=n-몇칸
    분모=1+몇칸
print(str(int(분자))+"/"+str(int(분모)))