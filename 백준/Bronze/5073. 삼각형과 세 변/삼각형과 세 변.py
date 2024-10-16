while True :
    a=list(map(int,input().split()))
    if a==[0,0,0]:
        break
    else:
        a.sort()
        if a[0]+a[1]>a[2]:
            if a[0]==a[1]==a[2]:
                print("Equilateral")
            elif a[0]==a[1] or a[0]==a[2] or a[1]==a[2]:
                print("Isosceles")
            else :
                print("Scalene")
        else:
            print("Invalid")