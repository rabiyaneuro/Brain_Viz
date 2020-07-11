# using Python 3.6.8 :: Anaconda, Inc.

import numpy as np
from visbrain.objects import ConnectObj, SceneObj, SourceObj, BrainObj

# First, we download a connectivity dataset consisting of the location of each
# node and the connectivity strength between every node

#Download 96x 96 tvb data
nodes = np.load("coords.npy")

#Download cv numpy array
edges_cv_a = np.load("cv_after.npy")

# Create the scene with a white background

#azimuth rotation on horizontal axis
CAM_STATE = dict(azimuth=0,        # azimuth angle
                 elevation=90,     # elevation angle
                 scale_factor=180  # distance to the camera
                 )

sc = SceneObj(bgcolor='white', size=(1600, 1000), camera_state=CAM_STATE)

# Colorbar default arguments. See `visbrain.objects.ColorbarObj`
CBAR_STATE = dict(cbtxtsz=12, txtsz=10., width=.1, cbtxtsh=3.,
                  rect=(-.3, -2., 1., 4.))
KW = dict(title_size=14., zoom=1.2)

# Color by connectivity strength
# First, we download a connectivity dataset consisting of the location of each
# node and the connectivity strength between those nodes. The first
# coloring method illustrated below consist in coloring connections based on
# a colormap

# Coloring method
color_by = 'strength'
# Because we don't want to plot every connections, we only keep connections
# above threshold

#applying mask for diff regions
mask = np.load("mask1.npy")
edges = np.where(mask, -999, edges_cv_a)

print(edges, edges.shape)

#diff levels for diff weights
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

if select_0.any():
	c_default = ConnectObj('default', nodes, edges, select=select_0, line_width=1.5, antialias =True, custom_colors = {None: "#686868"},color_by = color_by, cmap = "inferno")
	sc.add_to_subplot(c_default, row=0, col=0, zoom=0.1)

if select_1.any():
	c_default1 = ConnectObj('default', nodes, edges, select=select_1, line_width=1.5, antialias =True, custom_colors = {None: "black"},color_by = color_by, cmap = "inferno")
	sc.add_to_subplot(c_default1, row=0, col=0, zoom=0.1)

if select_2.any():
	c_default2 = ConnectObj('default', nodes, edges, select=select_2, line_width=1.6, antialias =True, custom_colors = {None: "rebeccapurple"},color_by = color_by, cmap = "inferno")
	sc.add_to_subplot(c_default2, row=0, col=0, zoom=0.1)

if select_3.any():
	c_default3 = ConnectObj('default', nodes, edges, select=select_3, line_width=1.7, antialias =True, custom_colors = {None: "mediumvioletred"},color_by = color_by, cmap = "inferno")
	sc.add_to_subplot(c_default3, row=0, col=0, zoom=0.1)


if select_4.any():
	c_default4 = ConnectObj('default', nodes, edges, select=select_4, line_width=1.8, antialias =True, custom_colors = {None: "darkorange"},color_by = color_by, cmap = "inferno")
	sc.add_to_subplot(c_default4, row=0, col=0, zoom=0.1)

# Then, we define the sourcess
#node size and color
s_obj = SourceObj('sources', nodes, radius_min=5., color="red")

# And add source to the scene
sc.add_to_subplot(s_obj, row=0, col=0, zoom=0.1)

sc.screenshot('cv_network.png', transparent=True)
print(edges_cv_a)
sc.preview()