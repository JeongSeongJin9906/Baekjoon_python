색종이개수=int(input())
array=[[0]*100 for i in range(100)]
for i in range(색종이개수):
    x,y=tuple(map(int,input().split()))
    for j in range(x,x+10):
        for k in range(y,y+10):
            array[j][k]=1
넓이=0
for i in range(100):
    넓이=넓이+array[i].count(1)
print(넓이)