a,b=map(int,input().split())
color=["B","W"]
chess_prototype=[]
for j in range(0,a):
    chess_line=[[color[i%2] for i in range(j,b+j)]]
    chess_prototype=chess_prototype+chess_line
bingo=[[0]*b for i in range(0,a)]
for k in range(0,a):
    current_chess=[list(input())]
    for m in range(0,b):
        if current_chess[0][m]==chess_prototype[k][m]:
            bingo[k][m]=1
        else:
            pass
check=[]
for m in range(0,b-7):
    for k in range(0,a-7):
        sum=0
        for i in range(0,8):
            sum=sum+bingo[k+i][m:m+8].count(1)
        check.append(min(sum,8*8-sum))
print(min(check))