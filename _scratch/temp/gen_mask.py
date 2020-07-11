
"""
This file generates and saves numpy arrays that are used by 'gen_net_fig.py':

- coords.npy
- mask1.npy
- cv_after.npy - needs name of text file with cv data as command line arg

To run this file use Python 2.7.16 :: Anaconda, Inc. because the TVB functions
don't work with Python 3
"""

from tvb.simulator.lab import connectivity
import pandas as pd
import numpy as np
import sys                

#Helper Functions########################################################################

def mask_data(mode, data):
    """
    mode is which mask you want:
    1: all-all
    2: cortical-cortical cnxns
    3: subcortico-subcortical cnxns
    4: cortical-subcortical cnxns
    
    data: the array you want to mask
    
    return: array of True/False of shape 'data' - False where you want to keep data and 
    True where you want to mask it
    """
    
    if mode == 1:
        mask = data==0
        return mask
    elif mode ==2:
        mask = np.zeros_like(data)
        for c in cortical_nodes: # set all cortical cnx to True
            mask[c,cortical_nodes] = True
            mask[cortical_nodes,c] = True
        mask = (mask*data!=0)==False # remove the cnx where weight is 0 then turn everything that is True to False
        return mask
    elif mode ==3:
        mask = np.zeros_like(data)
        for c in subcortical_nodes: 
            mask[c,subcortical_nodes] = True
            mask[subcortical_nodes,c] = True
        mask = (mask*data!=0)==False
        return mask
    elif mode ==4:
        mask = np.zeros_like(data)
        for c in cortical_nodes: 
            mask[c,subcortical_nodes] = True
            mask[subcortical_nodes,c] = True
        mask = (mask*weights_j!=0)==False
        return mask
    return

def gen_cv_array():
    # cv_after - generating numpy array from text ouput for cv
    # file name read from command line

    df = pd.read_csv(sys.argv[1], sep = "\t", header=None)
    temp = df.to_numpy()

    cv_after = np.ones((96,96))*-999
    cntr = 0
    for i in range(96):
        for j in range(96):
            cv_after[i,j] = temp[cntr,3]
            cntr= cntr + 1

    print(np.min(cv_after), np.max(cv_after), cv_after)
    
    return cv_after

def gen_coords():
    # get the coordinates data from TVB
    # sep is a regex expression bc the delimeter ranges from 1-3 white spaces

    df = pd.read_csv("connectivity_96/centres.txt", sep = " * ", header=None)
    coords_data = df.to_numpy()
    #coord_names = coords_data[:,0]
    coords_data = coords_data[:,1:4]
    
    return coords_data
    

def main():

    # save coords.npy
    np.save("coords.npy", gen_coords())    

    # save cv_after.npy
    cv_after = gen_cv_array()
    np.save("cv_after.npy",cv_after)

    # save mask1.npy

    # # How many cortical vs. subcortical nodes? (make sure correct modules are
    # # installed
    # conn_96 = connectivity.Connectivity.from_file('connectivity_96.zip')
    # cortical_nodes = np.nonzero(conn_96.cortical==True)[0]
    # subcortical_nodes = np.nonzero(conn_96.cortical==False)[0]

    #1  all connections
    mask = mask_data(1,cv_after)
    np.save("mask1.npy",mask)

main()