coordinate=[]
for i in range(3):
    coordinate.append(list(map(int,input().split())))
x_coordinate=[coordinate[i][0] for i in range(3)]
y_coordinate=[coordinate[i][1] for i in range(3)]
if x_coordinate.count(max(x_coordinate))==2:
    x=min(x_coordinate)
else:
    x=max(x_coordinate)
if y_coordinate.count(max(y_coordinate))==2:
    y=min(y_coordinate)
else:
    y=max(y_coordinate)
print(str(x),str(y))