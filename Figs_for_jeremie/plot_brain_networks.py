"""
Generating networks figs for jeremie's paper
====================================================

Plotting brain image with different networks shown

1. all connections
2. cortical-cortical cnxns
3. subcortico-subcortical cnxns
4. cortical-subcortical cnxns

"""
import numpy as np
from visbrain.objects import ConnectObj, SceneObj, SourceObj, BrainObj
from visbrain.io import download_file

cv_after = "cv_after.npy" # the array of cv after the changes
###############################################################################

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


# First, we download a connectivity dataset consisting of the location of each
# node and the connectivity strength between every node

#Download 96x 96 tvb data
nodes = np.load("coords.npy")

#Download Jeremie's cv weights data
edges_cv_a = np.load(cv_after)

# Because we don't want to plot every connections, we only keep connections
# above threshold

#diff levels for diff weights
# array of same size as the original array but filled with True and False
#edges = edges_cv_a

#choose the network num for which u want mask - data will not be shown in cells where mask is False
network_num = 4
mask = np.load("mask{}.npy".format(network_num))

# mask = np.where(mask, False, True)

edges = np.where(mask, -999, edges_cv_a)

if network_num ==1:
	col = 'blue'
if network_num ==2:
	col = 'green'
if network_num ==3:
	col = 'purple'
if network_num ==4:
	col = 'red'
#choose which color u want
alph = 0.7

#diff levels for diff weights
select0 = edges > 0
select00 = edges <= 10
select_0 = select0 == select00
print(select0, select00, select_0[select_0==True])
select1 = edges > 10
select11 = edges <=20
select_1 = select1 == select11

select2 = edges > 20
select22 = edges <=30
select_2 = select2 == select22

select3 = edges > 30
select33 = edges <=40
select_3 = select3 == select33

select4 = edges > 40
select44 = edges <=50
select_4 = select4 == select44

select_5 = edges > 50
################Different colors for diff strengths
# Define the connectivity object
#c_default = ConnectObj('default', nodes, edges, select=select, line_width=1.5, antialias =True, custom_colors = {None: col1}, alpha = alph)
#sc.add_to_subplot(c_default, row=0, col=0, zoom=0.1)


if select_0.any():
	c_default = ConnectObj('default', nodes, edges, select=select_0, line_width=1.5, antialias =True, custom_colors = {None: col}, alpha = alph)
	sc.add_to_subplot(c_default, row=0, col=0, zoom=0.1)

if select_1.any():
	c_default1 = ConnectObj('default', nodes, edges, select=select_1, line_width=1.6, antialias =True, custom_colors = {None: col}, alpha = alph)
	sc.add_to_subplot(c_default1, row=0, col=0, zoom=0.1)

if select_2.any():
	c_default2 = ConnectObj('default', nodes, edges, select=select_2, line_width=1.7, antialias =True, custom_colors = {None: col}, alpha = alph)
	sc.add_to_subplot(c_default2, row=0, col=0, zoom=0.1)

if select_3.any():
	c_default3 = ConnectObj('default', nodes, edges, select=select_3, line_width= 2, antialias =True, custom_colors = {None: col}, alpha = alph)
	sc.add_to_subplot(c_default3, row=0, col=0, zoom=0.1)

if select_4.any():
	c_default4 = ConnectObj('default', nodes, edges, select=select_4, line_width=2.5, antialias =True, custom_colors = {None: col}, alpha = alph)
	sc.add_to_subplot(c_default4, row=0, col=0, zoom=0.1)
if select_5.any():
	c_default4 = ConnectObj('default', nodes, edges, select=select_5, line_width=3, antialias =True, custom_colors = {None: col}, alpha = alph)
	sc.add_to_subplot(c_default4, row=0, col=0, zoom=0.1)


#if you want all connec to be same color use - custom_colors = {None: "green"}
# Then, we define the sourcess
#node size and color
s_obj = SourceObj('sources', nodes, radius_min=5., color="red")
sc.add_to_subplot(s_obj, row=0, col=0, zoom=0.1)


sc.screenshot('netowrk{}.png'.format(network_num), transparent=True)
print(edges)
sc.preview()