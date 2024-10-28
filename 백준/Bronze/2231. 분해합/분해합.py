number=input()
digit=len(number)
number=int(number)
divisors=[10**i+1 for i in range(digit-1,-1,-1)]
binary_array = [[int(bit) for bit in format(i, f'0{digit-1}b')]+[0] for i in range(2**(digit-1))]
def function(dividend,factor,array):
    x=[]
    for i in range(0,len(factor)):
        if dividend//factor[i]>9:
            x.append(str(9))
            dividend=dividend-(9)*factor[i]
        elif dividend//factor[i]==0 and array[i]==1:
            break
        else:
            x.append(str(dividend//(factor[i])-array[i]))
            dividend=dividend-(dividend//factor[i]-array[i])*(factor[i])
    if  dividend==0:
        return int("".join(x))
    else:
        return 0
result=[]
for s in range(0,2**(digit-1)):
    result.append(function(number,divisors,binary_array[s]))
result=set(result)
result=list(result)
result.sort()
if len(result)==1:
    print(result[0])
else:
    print(max(result[0],result[1]))
