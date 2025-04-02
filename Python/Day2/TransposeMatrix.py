a=[[1,2],[4,5],[7,8]]
b=[[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(a[i])):
        b[j][i]=a[i][j]
print(b)