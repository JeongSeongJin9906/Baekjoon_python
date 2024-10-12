x,y,w,h=tuple(map(int,input().split()))
print(min(min(w-x,x),min(h-y,y)))