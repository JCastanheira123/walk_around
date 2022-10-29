
import numpy as np
def stat(arg):
    median = np.median(arg)
    stdev = round(np.std(arg),2)
    maxi = np.max(arg)
    mini = np.min(arg)
    final_dist = arg[-1]
    print("Distancia final", final_dist)
    print('Max Distance = ', maxi)
    print('Min Distance = ', mini)
    print('Median',median)
    print('StdDev=',stdev)
    print("Dist_max", maxi,"Dist-min", mini)
    return