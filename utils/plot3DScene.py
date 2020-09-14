import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D

def plot3DScene(map_3d,imageRGB):

    scale = 0.0002
    map_3d = map_3d * scale

    downsample = 8

    points_x = map_3d[0,:].reshape(imageRGB.shape[0],imageRGB.shape[1])
    points_y = map_3d[1,:].reshape(imageRGB.shape[0],imageRGB.shape[1])
    points_z = map_3d[2,:].reshape(imageRGB.shape[0],imageRGB.shape[1])

    rows_down = imageRGB.shape[0]/downsample
    cols_down = imageRGB.shape[1]/downsample
    
    x_down = points_x[::downsample,::downsample]
    y_down = points_y[::downsample,::downsample]
    z_down = points_z[::downsample,::downsample]
    
    rgb_down = imageRGB[::downsample,::downsample,:]/255
    
    x_vec = x_down.reshape(int(rows_down*cols_down),1)
    y_vec = y_down.reshape(int(rows_down*cols_down),1)
    z_vec = z_down.reshape(int(rows_down*cols_down),1)
    rgb_vec = rgb_down.reshape(int(rows_down*cols_down),3)
    
    # Create figure
    fig = plt.figure()

    # Prepare figure for 3D data
    ax = fig.gca(projection='3d')

    # Name axes
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    
    # Set axes limits
    ax.set_xlim3d(-0.006,0.006)
    ax.set_ylim3d(-0.006,0.006)
    ax.set_zlim3d(0.006,0.016)
    
    ax.invert_zaxis()
    
    ax.view_init(elev=112, azim=-88)

    # Plot points
    ax.scatter(x_vec,y_vec,z_vec, c=rgb_vec)

    fig.show()
