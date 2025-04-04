def highaverage(a):
    avg=0
    for j in a[1]:
        avg+=j
    avg=avg/3
    return avg



students=[("Alice",[100,80,90]),("Bob",[80,60,30]),("David",[40,30,20])]
x1={}
ha=0
a=0
di={}
print(students[1][1])


######## Dictionaries of Students and their Grades ##########
for i in students:
    di[i[0]]=i[1]
print("Dictionaries of Students and their Grades",di)


############# Average of Individual Student #######
name=input("Enter Student Name")
print("Average grade for "+name+": ",di[name])

ps=[]

#####  Highest  Average ##########
for i in range(0,len(students)):
    a=highaverage(students[i])
    ps.append(a)
    if(a>ha):
        ha=a
        a=0
        x1[students[i][0]]=ha
    

print("Highest Average",x1)


###### Passed Students ########
print(ps)
count=0
for i in range(len(ps)):
    if ps[i]>=50:
        count+=1
print("Number of Students Passed",count)
