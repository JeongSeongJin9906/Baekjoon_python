bead_count=int(input())
bead_coordinate=[]
for i in range(bead_count):
    bead_coordinate.append(list(map(int,input().split())))
x_coordinate=[bead_coordinate[i][0] for i in range(bead_count)]
y_coordinate=[bead_coordinate[i][1] for i in range(bead_count)]
x_coordinate.sort()
y_coordinate.sort()
print((x_coordinate[-1]-x_coordinate[0])*(y_coordinate[-1]-y_coordinate[0]))