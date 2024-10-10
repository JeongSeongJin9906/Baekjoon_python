막대길이들=list(map(int,input().split()))
막대길이들.sort()
if 막대길이들[2]>=막대길이들[0]+막대길이들[1]:
    print(2*(막대길이들[0]+막대길이들[1])-1)
else:
    print(sum(막대길이들))