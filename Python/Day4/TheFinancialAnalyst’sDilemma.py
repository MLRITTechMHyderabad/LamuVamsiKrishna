import numpy as np


arr=np.random.randint(100,500,(30,5))
# print(arr)

#Average Stock prices
avg=np.mean(arr,axis=0)
print("Average Stock prices",avg)

#Highest Price Recorded 
max=np.max(arr)
min=np.min(arr)
loc=np.where(arr==max)
print("Location",loc,)
print("Highest Price Recorded :",max,"at","Day ",loc[0][0]+1,"Company",loc[1][0]+1)


#Normalized Prices
nor=((arr-min)/(max-min))
print("Normalized Prices :",nor)

#Risk Investment Days
# risk=np.where(arr<200)
# print(risk)
# for i in range(0,len(risk)):
#     print("Day",risk[0][0]+1,":",arr[risk])

risk=[]
for i,row in enumerate(arr):
    if np.any(row<200):
        risk.append((i+1,row[row<200]))
print("Risk Investment Days")
for day,prices in risk:
    print("Day",day,":",prices)