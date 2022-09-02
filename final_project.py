# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 10:59:51 2022

@author: Mohammadhossein Jafari 
"""
# The needed packeges are imported

import cv2
import PIL
from scipy.spatial import Voronoi
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from PIL import Image
import os
import torchvision.transforms as transforms
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
import torch
import io
image = []

# The needed information is gotten from the user

image_number= int(input("write the number of Voronoi images that you want to generate: " ))

explanation= "You have to fill the needed data for each of {} images".format(image_number)

print(explanation)

n_height= int(input("write the height number for images: "))

n_width=  int(input("write the width number for images: " ))

RGB_or_Gray_Scale = input("The output can be tensor of RGB images or GrayScale images. For RGB write RGB, for Gray-Scale write L: ")

Line_width=  int(input("What number for line_thickness do you prefer, write an integer such as 1 or 2? " ))

vertices= input('Do you like to show verticies, Write your answer with True or False? ')

showing_point= input('Do you like to show Voronoi points, Write your answer with True or False? ')


# the follwoing if_clauses provide needed information to generate images with the help of the voronoi_plot_2d

if vertices == 'True':
    vertices_show = True
else: 
    vertices_show = False




if showing_point == 'True':
    points_show = True
    voronoi_point_size = int(input("Please write the size of the voronoi point: "))
else: 
    points_show = False

if points_show == True:
     cell_point = voronoi_point_size
else:
    cell_point = False
    
n_seeds= int(input("write the number seeds for images: "))

np.random.seed(n_seeds)


#The list "colors" has a collection of colors, and cells and boundaries are collered based on the colors of this list.


colors = ['b','g','r', 'c', 'm', 'y', 'k']


for i in range(image_number):
    point_number= int(input("write the number of points for image number {}: ".format(i+1) )) 
    
    from scipy.spatial import Voronoi, voronoi_plot_2d
# make up data points
    points = np.random.rand(point_number,2)
# add 4 distant dummy points
    points = np.append(points, [[999,999], [-999,999], [999,-999], [-999,-999]], axis = 0)
# compute Voronoi tesselation
    vor = Voronoi(points)
# coloring the boundaries. All boundaries in an image have the same color
    def boundary_Colors():
        return np.random.choice(colors)    

# drawing the image by having the needed data    
    voronoi_plot_2d(vor, 
                    ax = None, 
                    show_points = points_show ,
                    show_vertices = vertices_show, 
                    line_colors= boundary_Colors(), 
                    line_width = Line_width, 
                    point_size= cell_point )
# colorize the cells
    def cell_Colors():
        return np.random.choice(colors)
    for region in vor.regions:
        if not -1 in region:
            polygon = [vor.vertices[i] for i in region]
            plt.fill(*zip(*polygon), cell_Colors())
# fix the range of axes
    plt.xlim([0,1]), plt.ylim([0,1])





    plt.savefig('image.png')
    

    plt.show()
    
    

    
# The image is loaded. It can be loaded as RGB or Gray_Scale. 
    img = Image.open('image.png').convert(RGB_or_Gray_Scale) # or RGB

    
# set up transformation to resize the image. The desired size of the image is implemented.
    resize = transforms.Resize([n_height, n_width])
    img = resize(img)
    type(img)
    to_tensor = transforms.ToTensor()

# apply transformation and convert to Pytorch tensor
    tensor = to_tensor(img)
    image.append(tensor)
    
image_tensor= torch.stack(image, dim=0) 




