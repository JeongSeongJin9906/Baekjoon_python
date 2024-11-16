word_list=list(input())
word="".join(word_list)
number=len(word)
diction={}
c=0
for i in word_list:
    diction[i]=set([])
for i in word_list:
    for j in range(c,number):
        current=word[c:j+1]
        diction[i].add(current)
    c=c+1
total=0
for key in diction:
    total=total+len(diction[key])
print(total)