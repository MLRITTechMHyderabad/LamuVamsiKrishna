import numpy as np

res=np.random.randint(10,50,(6,3))
print(res)
max=np.max(res)
loc=np.where(res==max)
print(loc)
total=np.sum(res,axis=0)
print("Total resources required oxygen:",total[0],"water:",total[1],"Food:",total[2])
print("Highest consumption in a month: Water ",max,"in month",loc[0][0]+1)

sd=np.std(res,axis=0)
print("Standard deviation of consumption: Oxygen: ",sd[0],"water:",sd[1],"Food",sd[2])
print(np.transpose(res))
