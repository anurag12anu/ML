import numpy as np
from scipy import stats

speed=[99,86,88,87,111,86,103,94,78,77,85,86]

means=np.mean(speed)


print(means)
meadians=np.median(speed)
print(meadians)

modes=stats.mode(speed)
print(modes)