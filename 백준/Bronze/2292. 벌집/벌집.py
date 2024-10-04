가야할곳=int(input())
i=1
if 가야할곳==1:
   print(1)
else:
    while True:
        if 3*i**2-3*i+1<가야할곳<=3*i**2+3*i+1:
            i=i+1
            break
        else:
            i=i+1
    print(i)