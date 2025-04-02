li=[1,33,4,5,6,4,5,5,5,5,33,33,33]
c=li[0]
d={}
outcount =0
for i in range(len(li)):
    incount=0
    b=li[i]
    for j in range(len(li)):
        if li[i]==li[j]:
            incount+=1
    if incount>outcount:
        d[c]=incount
        c=li[i]
print(d)