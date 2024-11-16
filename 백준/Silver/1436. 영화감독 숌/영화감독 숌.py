number=int(input())
initial=665
count=0
while True :
    initial=initial+1
    if "666" in str(initial):
        count=count+1
    if count==number:
        print(initial)
        break