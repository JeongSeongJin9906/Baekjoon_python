number_list=list(map(int,input().split()))
first=number_list[0:3]
second=number_list[3:6]
a=first[0]
b=second[0]
if a==0:
    y=first[2]/first[1]
    x=(second[2]-second[1]*y)/second[0]
elif b==0:
    y=second[2]/second[1]
    x=(first[2]-first[1]*y)/first[0]
else:
    first=[i*b for i in first]
    second=[i*a for i in second]
    y=(first[2]-second[2])/(first[1]-second[1])
    x=(first[2]-first[1]*y)/(first[0])
print(int(x),int(y))