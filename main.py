import route_constr as roucs
import random
import numpy as np
import graphic as grph
list_dist = []
import time
start = time.time()
essays = 500
for c in range(0,essays):
    steps = random.randint(100,1000)
    final_dist = roucs.df(essays,steps)
    list_dist.append(final_dist)
fig = grph.grf(list_dist)
print('Tempo = ', time.time() - start)
#print(list_dist)# [steps, dist]
#print(sorted(list_dist))