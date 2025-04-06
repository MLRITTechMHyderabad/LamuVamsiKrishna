import numpy as np
score=np.random.randint(10,40,(5,10))
print(score)

avg=np.mean(score,axis=1)
print("Average Points per game:",avg)

sum=np.sum(score,axis=1)
best_player=np.argmax(sum)
worst_player=np.argmin(sum)

print("Best Performing Player",best_player+1,"Total:",sum[best_player],"points")
print("Worst Performing Player",worst_player+1,"Total:",sum[worst_player],"points")

