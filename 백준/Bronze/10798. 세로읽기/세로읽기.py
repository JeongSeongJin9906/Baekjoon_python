문자열리스트=[]
for i in range(0,5):
    문자열리스트.append(list(input()))
가장긴문자열의길이=max(list(len(문자열리스트[i]) for i in range(0,5)))
새로만들어진문자열리스트=[]
for i in range(0,가장긴문자열의길이):
    for j in range(0,5):
        try:
            새로만들어진문자열리스트.append(문자열리스트[j][i])
        except:
            continue
print("".join(새로만들어진문자열리스트))