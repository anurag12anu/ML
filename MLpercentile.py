import numpy as np

import scipy 
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

age=np.percentile(ages,90)
print(age)