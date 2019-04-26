"""
Connectivity object (ConnectObj) : complete tutorial
====================================================

Illustration of the main functionalities and inputs of the connectivity object:

    * Color connectivity links according to connectivity strength
    * Color connectivity links according to the number of connections per node
    * Color connectivity links using custom colors
"""
import numpy as np
from visbrain.objects import ConnectObj, SceneObj, SourceObj, BrainObj
from visbrain.io import download_file

###############################################################################
# Download data
###############################################################################
# First, we download a connectivity dataset consisting of the location of each
# node and the connectivity strength between every node

# Download data (original code)
#arch = np.load(download_file('phase_sync_delta.npz', astype='example_data'))
#nodes, edges = arch['nodes'], arch['edges']

#Download 96x 96 tvb data
nodes, edges = np.load("coords.npy"), np.load("weights.npy")

#Download Jeremie's weights data
edges_j = np.load("weights_j.npy")

#Download Jeremie's weights data
edges_cv_b = np.load("cv_before.npy")
edges_cv_a = np.load("cv_after.npy")

###############################################################################
# Define the scene
###############################################################################

# Create the scene with a black background
#azimuth rotation on horizontal axis
CAM_STATE = dict(azimuth=90,        # azimuth angle
                 elevation=0,     # elevation angle
                 )
#grey color - '#D3D3D3'
sc = SceneObj(bgcolor='#D3D3D3', size=(1500, 1100), camera_state=CAM_STATE)
# sc = SceneObj(size=(1500, 600))

# Colorbar default arguments. See `visbrain.objects.ColorbarObj`
CBAR_STATE = dict(cbtxtsz=12, txtsz=10., width=.1, cbtxtsh=3.,
                  rect=(-.3, -2., 1., 4.))
KW = dict(title_size=14., zoom=1.2)

###############################################################################
# Color by connectivity strength
###############################################################################
# First, we download a connectivity dataset consisting of the location of each
# node (iEEG site) and the connectivity strength between those nodes. The first
# coloring method illustrated bellow consist in coloring connections based on
# a colormap

# Coloring method
color_by = 'strength'
# Because we don't want to plot every connections, we only keep connections
# above threshold
select = edges >0 

################Different colors for diff strengths
# Define the connectivity object
c_default = ConnectObj('default', nodes, edges_cv_b, select=select, line_width=2., antialias =True, dynamic = (0,0.5), custom_colors = {None: "black"},color_by = color_by, cmap = "inferno")
#if you want all connec to be same color use - custom_colors = {None: "green"}
# Then, we define the sources
#node size and color
s_obj = SourceObj('sources', nodes, color='#000000', radius_min=5.)
#title
sc.add_to_subplot(c_default, row=0, col=0, zoom=0.1)

# And add connect, source and brain objects to the scene
sc.add_to_subplot(s_obj, row=0, col=0, zoom=0.1)
sc.add_to_subplot(BrainObj('B3'),row=0, col=0, use_this_cam=True)
#, use_this_cam=True
from visbrain.objects import ColorbarObj
cb = ColorbarObj(c_default, **CBAR_STATE)
sc.add_to_subplot(cb, width_max=200, row=0, col=1)

  # clim=(4., 78.2), vmin=10.,
  #                 vmax=72., cblabel='Colorbar title', under='gray',
  #                 over='red', txtcolor='black', cbtxtsz=40, cbtxtsh=2.,
  #                 txtsz=20., width=.04)


sc.preview()
#sc.screenshot("test.jpg")

################Different transparency for diff strengths (one color)
# Define the connectivity object
# c_default = ConnectObj('default', nodes, edges, select=select, line_width=0.5,dynamic=(0, 1),
#                        cmap='viridis',custom_colors = {None: "green"})
# # Then, we define the sources
# #node size and color
# s_obj = SourceObj('sources', nodes, color='#000000', radius_min=10.)
# #title
# sc.add_to_subplot(c_default, row=0, col=0, zoom=0.1)

# # And add connect, source and brain objects to the scene
# sc.add_to_subplot(s_obj, row=0, col=0, zoom=0.1)
# sc.add_to_subplot(BrainObj('B3'),row=0, col=0, zoom=0.1)
# #, use_this_cam=True
# from visbrain.objects import ColorbarObj
# cb = ColorbarObj('s_obj', **CBAR_STATE)
# sc.add_to_subplot(cb, width_max=200, row=0, col=1)

#   # clim=(4., 78.2), vmin=10.,
#   #                 vmax=72., cblabel='Colorbar title', under='gray',
#   #                 over='red', txtcolor='black', cbtxtsz=40, cbtxtsh=2.,
#   #                 txtsz=20., width=.04)


# sc.preview()

"""
###############################################################################
# Color by number of connections per node
###############################################################################
# The next coloring method consist in set a color according to the number of
# connections per node. Here, we also illustrate that colors can also by
# `dynamic` (i.e stronger connections are opaque and weak connections are more
# translucent)

# Coloring method
color_by = 'count'
# Weak connections -> alpha = .1 // strong connections -> alpha = 1.
dynamic = (.1, 1.)
# Define the connectivity and source object
c_count = ConnectObj('default', nodes, edges, select=select, line_width=4.,
                     color_by=color_by, antialias=True, dynamic=dynamic)
s_obj_c = SourceObj('sources', nodes, color='olive', radius_min=10.,
                    symbol='square')
# And add connect, source and brain objects to the scene
sc.add_to_subplot(c_count, row=0, col=1,
                  title='Color by number of connections per node')
sc.add_to_subplot(s_obj_c, use_this_cam=True, row=0, col=1)
sc.add_to_subplot(BrainObj('B3'), use_this_cam=True, row=0, col=1)

###############################################################################
# Custom colors
###############################################################################
# Finally, you can define your own colors which mean that for a specific
# connectivity strength, you can manually set a unique color. The provided
# dataset has values between [0., 1.]

# First, we take a copy of the connectivity array
edges_copy = edges.copy()
# Then, we force edges to take fixed values
# ====================   =========  ===========
# Condition              New value  Color
# ====================   =========  ===========
# edges >= 0.8              4.      red
# edges in [.78, .8[        3.      orange
# edges in [.74, .78[       2.      blue
# Others                    -       lightgray
# ====================   =========  ===========
edges_copy[edges_copy >= .8] = 4.
edges_copy[np.logical_and(edges_copy >= .78, edges_copy < .8)] = 3.
edges_copy[np.logical_and(edges_copy >= .74, edges_copy < .78)] = 2.
# Now we use a dctionary to set one color per value.
ccol = {
    None: 'lightgray',
    2.: 'blue',
    3.: 'orange',
    4.: 'red'
}

# Define the connectivity and source objects
c_cuscol = ConnectObj('default', nodes, edges_copy, select=edges > .7,
                      custom_colors=ccol)
s_obj_cu = SourceObj('sources', nodes, color='slategray', radius_min=10.,
                     symbol='ring')
# Add objects to the scene
sc.add_to_subplot(c_cuscol, row=0, col=2, title='Custom colors')
sc.add_to_subplot(s_obj_cu, row=0, col=2)
sc.add_to_subplot(BrainObj('white'), use_this_cam=True, row=0, col=2)

# Finally, display the scene
sc.preview()

"""