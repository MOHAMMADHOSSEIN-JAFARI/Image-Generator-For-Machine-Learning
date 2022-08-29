# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 10:59:51 2022

@author: Mohammadhossein Jafari 
"""
import cv2
import PIL
from scipy.spatial import Voronoi
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from PIL import Image
import os
import torchvision.transforms as transforms

image = []


image_number= int(input("write the number of images: " ))

explanation= "You have to fill the needed data for each of {} images".format(image_number)
print(explanation)
n_height= int(input("write the number height for images: "))
n_width=  int(input("write the number width for images: " ))
RGB_or_Gray_Scale = input("The output can be tensor of RGB images or GrayScale images. For RGB write RGB, for Gray-Scale write L: ")
Line_width=  int(input("What number for line width do you prefer, write an integer? " ))
n_seeds= int(input("write the number seeds for images: "))





colors = ['b','g','r', 'c', 'm', 'y', 'k']
"""
def boundary_Colors():
        return np.random.choice(colors)

"""
for i in range(image_number):
    point_number= int(input("write the number of points for image number {}: ".format(i+1) )) 
    np.random.seed(n_seeds)
    from scipy.spatial import Voronoi, voronoi_plot_2d
# make up data points
    points = np.random.rand(point_number,2)
# add 4 distant dummy points
    points = np.append(points, [[999,999], [-999,999], [999,-999], [-999,-999]], axis = 0)
# compute Voronoi tesselation
    vor = Voronoi(points)
# plot
# vor.regions
    def boundary_Colors():
        return np.random.choice(colors)    
    voronoi_plot_2d(vor, 
                    ax = None, 
                    show_points = None ,
                    show_vertices = None, 
                    line_colors= boundary_Colors(), 
                    line_width = Line_width, 
                    point_size= 2 )
# colorize
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
    
    import torch

    
# load image in RGB mode (png files contains additional alpha channel)
    img = Image.open('image.png').convert(RGB_or_Gray_Scale) # or RGB

    
# set up transformation to resize the image
    resize = transforms.Resize([n_height, n_width])
    img = resize(img)
    type(img)
    to_tensor = transforms.ToTensor()

# apply transformation and convert to Pytorch tensor
    tensor = to_tensor(img)
    image.append(tensor)
    
image_tensor= torch.stack(image, dim=0) 


