###############################################################################
# cv_after - generating numpy array from text ouput for cv
# file name read from command line
###############################################################################
df = pd.read_csv(sys.argv[1], sep = "\t", header=None)
temp = df.to_numpy()

cv_after = np.ones((96,96))*-999
cntr = 0
for i in range(96):
    for j in range(96):
        cv_after[i,j] = temp[cntr,3]
        cntr= cntr + 1

print(np.min(cv_after), np.max(cv_after))
print(cv_after)
np.save("cv_after.npy",cv_after)

import * from gen_mask

###############################################################################
#coords - get the coordinates data from TVB
###############################################################################
# sep is a regex expression bc the delimeter ranges from 1-3 white spaces

import pandas as pd
import numpy as np

df = pd.read_csv("connectivity_96/centres.txt", sep = " * ", header=None)
coords_data = df.to_numpy()
#coord_names = coords_data[:,0]
coords_data = coords_data[:,1:4]
#np.save("coords.npy", coords_data)

###############################################################################
