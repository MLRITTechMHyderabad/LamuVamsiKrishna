import random
d1=[1,2,3,4,5,6]
d2=[1,2,3,4,5,6]
li=[]
for i in d1:
    for j in d2:
        li.append((i,j))
print(li)

di={}
for i in range(2,13):
    c=0
    for j in li:
        if i==j[0]+j[1]:
            c+=1
    di[i]=c/len(li)
print(di)

ll=[]
p1=0
p2=0
rounds=int(input("Enter Number of Rounds"))
for i in range(rounds):
    x1=random.randint(1,6)
    x2=random.randint(1,6)
    y1=random.randint(1,6)
    y2=random.randint(1,6)
    print(x1)
    print(x2)
    print(y1)
    print(y2)
    x=x1+x2
    y=y1+y2
    if(di[x]<di[y]):
        p1+=1
    elif(di[x]==di[y]):
        p1+=0
        p2+=0
    else:
        p2+=1


if p1>p2:
    print("Player 1")
elif p1<p2:
    print("Player 2")
else:
    print("draw")
