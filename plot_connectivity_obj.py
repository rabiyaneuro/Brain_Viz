"""
Generating networks figs for jeremie's paper
====================================================

1. Network before cv
2. Network after cv
3. Plain brain image

"""
import numpy as np
from visbrain.objects import ConnectObj, SceneObj, SourceObj, BrainObj
from visbrain.io import download_file

###############################################################################
# 1. Network before cv
###############################################################################
# First, we download a connectivity dataset consisting of the location of each
# node and the connectivity strength between every node

#Download 96x 96 tvb data
nodes = np.load("coords.npy")

#Download Jeremie's cv weights data
edges_cv_b = np.load("cv_before.npy")

# Create the scene with a black background

#azimuth rotation on horizontal axis
CAM_STATE = dict(azimuth=0,        # azimuth angle
                 elevation=90,     # elevation angle
                 scale_factor=180  # distance to the camera
                 )
#grey color - '#D3D3D3'
sc = SceneObj(bgcolor='white', size=(1600, 1000), camera_state=CAM_STATE)
# sc = SceneObj(size=(1500, 600))

# Colorbar default arguments. See `visbrain.objects.ColorbarObj`
CBAR_STATE = dict(cbtxtsz=12, txtsz=10., width=.1, cbtxtsh=3.,
                  rect=(-.3, -2., 1., 4.))
KW = dict(title_size=14., zoom=1.2)

# Color by connectivity strength
# First, we download a connectivity dataset consisting of the location of each
# node (iEEG site) and the connectivity strength between those nodes. The first
# coloring method illustrated bellow consist in coloring connections based on
# a colormap

# Coloring method
color_by = 'strength'
# Because we don't want to plot every connections, we only keep connections
# above threshold

#diff levels for diff weights
edges = edges_cv_b
select0 = edges > 0
select00 = edges <10
select_0 = select0 == select00

################Different colors for diff strengths
# Define the connectivity object
c_default = ConnectObj('default', nodes, edges, select=select_0, line_width=1.5, antialias =True, custom_colors = {None: "#686868"},color_by = color_by, cmap = "inferno")

#if you want all connec to be same color use - custom_colors = {None: "green"}
# Then, we define the sourcess
#node size and color
s_obj = SourceObj('sources', nodes, radius_min=5., color="red")
sc.add_to_subplot(c_default, row=0, col=0, zoom=0.1)
sc.add_to_subplot(s_obj, row=0, col=0, zoom=0.1)

sc.screenshot('cv_before.png', transparent=True)
print(edges_cv_b)
sc.preview()

###############################################################################
# 2. Network after cv
###############################################################################
# First, we download a connectivity dataset consisting of the location of each
# node and the connectivity strength between every node

#Download 96x 96 tvb data
nodes = np.load("coords.npy")

#Download Jeremie's cv weights data
edges_cv_a = np.load("cv_after.npy")

# Create the scene with a black background

#azimuth rotation on horizontal axis
CAM_STATE = dict(azimuth=0,        # azimuth angle
                 elevation=90,     # elevation angle
                 scale_factor=180  # distance to the camera
                 )
#grey color - '#D3D3D3'
sc = SceneObj(bgcolor='white', size=(1600, 1000), camera_state=CAM_STATE)

# Colorbar default arguments. See `visbrain.objects.ColorbarObj`
CBAR_STATE = dict(cbtxtsz=12, txtsz=10., width=.1, cbtxtsh=3.,
                  rect=(-.3, -2., 1., 4.))
KW = dict(title_size=14., zoom=1.2)

# Color by connectivity strength
# First, we download a connectivity dataset consisting of the location of each
# node (iEEG site) and the connectivity strength between those nodes. The first
# coloring method illustrated bellow consist in coloring connections based on
# a colormap

# Coloring method
color_by = 'strength'
# Because we don't want to plot every connections, we only keep connections
# above threshold

#diff levels for diff weights
edges = edges_cv_a
select0 = edges > 0
select00 = edges <10
select_0 = select0 == select00

select1 = edges > 10
select11 = edges <20
select_1 = select1 == select11

select2 = edges > 20
select22 = edges <30
select_2 = select2 == select22

select3 = edges > 30
select33 = edges <40
select_3 = select3 == select33

select_4 = edges > 40
################Different colors for diff strengths
# Define the connectivity object
c_default = ConnectObj('default', nodes, edges, select=select_0, line_width=1.5, antialias =True, custom_colors = {None: "#686868"},color_by = color_by, cmap = "inferno")
c_default1 = ConnectObj('default', nodes, edges, select=select_1, line_width=1.6, antialias =True, custom_colors = {None: "black"},color_by = color_by, cmap = "inferno")
c_default2 = ConnectObj('default', nodes, edges, select=select_2, line_width=1.7, antialias =True, custom_colors = {None: "rebeccapurple"},color_by = color_by, cmap = "inferno")
c_default3 = ConnectObj('default', nodes, edges, select=select_3, line_width=1.8, antialias =True, custom_colors = {None: "mediumvioletred"},color_by = color_by, cmap = "inferno")
c_default4 = ConnectObj('default', nodes, edges, select=select_4, line_width=2.5, antialias =True, custom_colors = {None: "darkorange"},color_by = color_by, cmap = "inferno")


#if you want all connec to be same color use - custom_colors = {None: "green"}
# Then, we define the sourcess
#node size and color
s_obj = SourceObj('sources', nodes, radius_min=5., color="red")
# black color nodes = color='#000000'
#title
sc.add_to_subplot(c_default, row=0, col=0, zoom=0.1)
sc.add_to_subplot(c_default1, row=0, col=0, zoom=0.1)
sc.add_to_subplot(c_default2, row=0, col=0, zoom=0.1)
sc.add_to_subplot(c_default3, row=0, col=0, zoom=0.1)
sc.add_to_subplot(c_default4, row=0, col=0, zoom=0.1)

# And add connect, source and brain objects to the scene
sc.add_to_subplot(s_obj, row=0, col=0, zoom=0.1)

sc.screenshot('cv_after.png', transparent=True)
print(edges_cv_a)
sc.preview()

###############################################################################
# 3. Plain brain
###############################################################################

# Create the scene 

sc = SceneObj(bgcolor='#D3D3D3', size=(1600, 1000))
b_obj = BrainObj('B3')
sc.add_to_subplot(b_obj,row=0, col=0, use_this_cam=True)
#sc.screenshot('plain_brain.png', transparent=True)
sc.preview()