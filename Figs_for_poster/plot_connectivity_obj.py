"""
Generating networks figs for poster
====================================================
1. Target Network
2. Estimated Network
"""
import numpy as np
import random
from visbrain.objects import ConnectObj, SceneObj, SourceObj, BrainObj
from visbrain.io import download_file

#CHOOSE NETWORK (change according to which fig you want to generate)
NETWORK = 1
EST = 3 #1: correlation, 2: pli, 3: pli+corr

# Download data
# arch = np.load(download_file('phase_sync_delta.npz', astype='example_data'))
# temp= arch['nodes']


# indx = []
# for i in range(10):
#     indx.append(random.randint(1,100))
# nodes = temp[indx,:]
# np.save("coords2.npy", nodes)


nodes = np.load("coords2.npy")

JOB = ['990797','990798', '990799',
       '1061083', '1061085','1061086',
       '1061632','1061633','1061635']

# #Download coordinates data (10 nodes same for all)
# nodes = np.load("coords.npy")
def p2matrix(p, nodes_n):
    """fills in upper and lower triangle of matrix with p, leaving the diagonal with 0s"""
    ind = 0
    wmat = np.zeros((nodes_n, nodes_n))
    for row in range(0,nodes_n):
        for col in range(row+1, nodes_n):
            wmat[row,col] = p[ind]
            wmat[col,row] = p[ind]
            ind += 1
    return wmat


#Edge/cv data
if NETWORK ==1:
	edges_cv_b = np.ones((10,10))*0.5
	np.fill_diagonal(edges_cv_b,0)

	if EST == 1:
		edges_cv_a  = np.load(JOB[0]+".npy")
	elif EST == 2:
		edges_cv_a  = np.load(JOB[3]+".npy")
	elif EST == 3:
		edges_cv_a  = np.load(JOB[6]+".npy")
elif NETWORK ==2:
	seed2 = 200
	num_dim = int((((10**2)-10)/2))
	rng = np.random.RandomState(seed2)
	c_mat_v = rng.uniform(low = 500,high=10000, size=(num_dim))*0.001
	edges_cv_b = p2matrix(c_mat_v, 10)
	np.fill_diagonal(edges_cv_b,0)

	if EST == 1:
		edges_cv_a  = np.load(JOB[1]+".npy")
	elif EST == 2:
		edges_cv_a  = np.load(JOB[4]+".npy")
	elif EST == 3:
		edges_cv_a  = np.load(JOB[7]+".npy")
elif NETWORK ==3:
	edges_cv_b = np.ones((10,10))*10
	np.fill_diagonal(edges_cv_b,0)
	if EST == 1:
		edges_cv_a  = np.load(JOB[2]+".npy")
	elif EST == 2:
		edges_cv_a  = np.load(JOB[5]+".npy")
	elif EST == 3:
		edges_cv_a  = np.load(JOB[8]+".npy")

# Create the scene with a black background

#azimuth rotation on horizontal axis
CAM_STATE = dict(azimuth=0,        # azimuth angle
                 elevation=90,     # elevation angle
                 scale_factor=180  # distance to the camera
                 )
# top view - 0, 90, 180
# front = 0, 0 ,180
# 90, 0, 180
#grey color - '#D3D3D3'
sc = SceneObj(bgcolor='white', size=(1600, 1000), camera_state=CAM_STATE)
# sc = SceneObj(size=(1500, 600))

# Colorbar default arguments. See `visbrain.objects.ColorbarObj`
CBAR_STATE = dict(cbtxtsz=12, txtsz=10., width=.1, cbtxtsh=3.,
                  rect=(-.3, -2., 1., 4.))
KW = dict(title_size=14., zoom=1.2)

#diff levels for diff weights
edges = edges_cv_b
print(edges)
bndries = [0.5, 2,4, 6, 8, 9, 10]
width  = 3


###############################################################################
# 1. Target Network
###############################################################################

# select0 = edges >=bndries[0]
# select00 = edges <bndries[1]
# select_0 = select0 == select00

# select1 = edges >= bndries[1]
# select11 = edges <bndries[2]
# select_1 = select1 == select11

# select2 = edges >= bndries[2]
# select22 = edges <bndries[3]
# select_2 = select2 == select22

# select3 = edges >= bndries[3]
# select33 = edges <bndries[4]
# select_3 = select3 == select33

# select4 = edges >= bndries[4]
# select44 = edges <bndries[5]
# select_4 = select4 == select44

# select_5 = edges >= bndries[5]

# # select5 = edges >= bndries[5]
# # select55 = edges <bndries[6]
# # select_5 = select5 == select55

# # select6 = edges >= bndries[6]
# # select66 = edges <bndries[7]
# # select_6 = select6 == select66

# # select_7 = edges > bndries[7]

# ################Different colors for diff strengths
# # Define the connectivity object
# if select_0.any():
# 	c_default = ConnectObj('default', nodes, edges, select=select_0, line_width=width, 
# 		antialias =True, custom_colors = {None: "midnightblue"})
# 	sc.add_to_subplot(c_default, row=0, col=0, zoom=0.1)

# if select_1.any():
# 	c_default1 = ConnectObj('default', nodes, edges, select=select_1, line_width=width, 
# 		antialias =True, custom_colors = {None: "navy"})
# 	sc.add_to_subplot(c_default1, row=0, col=0, zoom=0.1)

# if select_2.any():
# 	c_default2 = ConnectObj('default', nodes, edges, select=select_2, line_width=width, 
# 		antialias =True, custom_colors = {None: "mediumblue"})
# 	sc.add_to_subplot(c_default2, row=0, col=0, zoom=0.1)

# if select_3.any():
# 	c_default3 = ConnectObj('default', nodes, edges, select=select_3, line_width=width, 
# 		antialias =True, custom_colors = {None: "dodgerblue"})
# 	sc.add_to_subplot(c_default3, row=0, col=0, zoom=0.1)


# if select_4.any():
# 	c_default4 = ConnectObj('default', nodes, edges, select=select_4, line_width=width, 
# 		antialias =True, custom_colors = {None: "steelblue"})
# 	sc.add_to_subplot(c_default4, row=0, col=0, zoom=0.1)

# if select_5.any():
# 	c_default5 = ConnectObj('default', nodes, edges, select=select_5, line_width=width, 
# 		antialias =True, custom_colors = {None: "skyblue"})
# 	sc.add_to_subplot(c_default5, row=0, col=0, zoom=0.1)

# # if select_6.any():
# # 	c_default6 = ConnectObj('default', nodes, edges, select=select_6, line_width=width, 
# # 		antialias =True, custom_colors = {None: "deepskyblue"})
# # 	sc.add_to_subplot(c_default6, row=0, col=0, zoom=0.1)

# # if select_7.any():
# # 	c_default7 = ConnectObj('default', nodes, edges, select=select_7, line_width=width, 
# # 		antialias =True, custom_colors = {None: "aqua"})
# # 	sc.add_to_subplot(c_default7, row=0, col=0, zoom=0.1)

# # ['midnightblue', 'navy', 'mediumblue', 'blue','dodgerblue','deepskyblue']
# # old- ['#686868', 'black', 'rebeccapurple', 'mediumvioletred', 'darkorange']
# # '#686868', 'blue', 'cyan', 'springgreen', 'yellow','orange', 'red', 'maroon'
# # '#686868', 'black', 'blue', 'green', 'yellow','orange', 'red', 'maroon'
# #if you want all connec to be same color use - custom_colors = {None: "green"}

# # Then, we define the sourcess
# #node size and color
# s_obj = SourceObj('sources', nodes, radius_min=5., color="red")
# # black color nodes = color='#000000'
# #title

# # And add source to the scene
# sc.add_to_subplot(s_obj, row=0, col=0, zoom=0.1)

# name = 'targ_net{}.png'.format(NETWORK)
# #sc.screenshot(name, transparent=True)
# print(edges_cv_b)
# sc.preview()

##############################################################################################################################################################

# 2. Estimated Network
##############################################################################################################################################################

edges = edges_cv_a
print(edges)

select0 = edges >=bndries[0]
select00 = edges <bndries[1]
select_0 = select0 == select00

select1 = edges >= bndries[1]
select11 = edges <bndries[2]
select_1 = select1 == select11

select2 = edges >= bndries[2]
select22 = edges <bndries[3]
select_2 = select2 == select22

select3 = edges >= bndries[3]
select33 = edges <bndries[4]
select_3 = select3 == select33

select4 = edges >= bndries[4]
select44 = edges <bndries[5]
select_4 = select4 == select44

select_5 = edges >= bndries[5]


# select5 = edges >= bndries[5]
# select55 = edges <bndries[6]
# select_5 = select5 == select55

# select6 = edges >= bndries[6]
# select66 = edges <bndries[7]
# select_6 = select6 == select66

# select_7 = edges > bndries[7]

################Different colors for diff strengths
# Define the connectivity object
if select_0.any():
	c_default = ConnectObj('default', nodes, edges, select=select_0, line_width=width, 
		antialias =True, custom_colors = {None: "midnightblue"})
	sc.add_to_subplot(c_default, row=0, col=0, zoom=0.1)

if select_1.any():
	c_default1 = ConnectObj('default', nodes, edges, select=select_1, line_width=width, 
		antialias =True, custom_colors = {None: "navy"})
	sc.add_to_subplot(c_default1, row=0, col=0, zoom=0.1)

if select_2.any():
	c_default2 = ConnectObj('default', nodes, edges, select=select_2, line_width=width, 
		antialias =True, custom_colors = {None: "mediumblue"})
	sc.add_to_subplot(c_default2, row=0, col=0, zoom=0.1)

if select_3.any():
	c_default3 = ConnectObj('default', nodes, edges, select=select_3, line_width=width, 
		antialias =True, custom_colors = {None: "dodgerblue"})
	sc.add_to_subplot(c_default3, row=0, col=0, zoom=0.1)


if select_4.any():
	c_default4 = ConnectObj('default', nodes, edges, select=select_4, line_width=width, 
		antialias =True, custom_colors = {None: "steelblue"})
	sc.add_to_subplot(c_default4, row=0, col=0, zoom=0.1)

if select_5.any():
	c_default5 = ConnectObj('default', nodes, edges, select=select_5, line_width=width, 
		antialias =True, custom_colors = {None: "skyblue"})
	sc.add_to_subplot(c_default5, row=0, col=0, zoom=0.1)

# if select_6.any():
# 	c_default6 = ConnectObj('default', nodes, edges, select=select_6, line_width=width, antialias =True, custom_colors = {None: "deepskyblue"})
# 	sc.add_to_subplot(c_default6, row=0, col=0, zoom=0.1)

# if select_7.any():
# 	c_default7 = ConnectObj('default', nodes, edges, select=select_7, line_width=width, antialias =True, custom_colors = {None: "aqua"})
# 	sc.add_to_subplot(c_default7, row=0, col=0, zoom=0.1)

# Then, we define the sourcess
#node size and color
s_obj = SourceObj('sources', nodes, radius_min=5., color="red")
# black color nodes = color='#000000'
#title

# And add source to the scene
sc.add_to_subplot(s_obj, row=0, col=0, zoom=0.1)
name = 'est_net{}_meth{}.png'.format(NETWORK,EST)
print(name)
sc.screenshot(name, transparent=True)
print("a",np.mean(edges_cv_a[edges_cv_a!=0]))
sc.preview()