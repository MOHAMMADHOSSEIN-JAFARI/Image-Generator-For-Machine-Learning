# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 17:16:52 2022

@author: unimi
"""



import cv2
from scipy.spatial import Voronoi
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
#import torch
import os





from scipy.spatial import Voronoi, voronoi_plot_2d
# make up data points
points = np.random.rand(20,2)
# add 4 distant dummy points
points = np.append(points, [[999,999], [-999,999], [999,-999], [-999,-999]], axis = 0)
# compute Voronoi tesselation
vor = Voronoi(points)
# plot
voronoi_plot_2d(vor, line_colors='white')
# colorize
for region in vor.regions:
    if not -1 in region:
        polygon = [vor.vertices[i] for i in region]
        plt.fill(*zip(*polygon))
# fix the range of axes
plt.xlim([0,1]), plt.ylim([0,1])

plt.show()

plt.savefig('x.png')

######
import torchvision.transforms as transforms
from PIL import Image
import torch
# load image in RGB mode (png files contains additional alpha channel)
img = Image.open('x.png').convert('RGB')

# set up transformation to resize the image
resize = transforms.Resize([224, 224])
img = resize(img)
to_tensor = transforms.ToTensor()

# apply transformation and convert to Pytorch tensor
tensor = to_tensor(img)
# torch.Size([3, 224, 224])

# add another dimension at the front to get NCHW shape
tensor = tensor.unsqueeze(0)
