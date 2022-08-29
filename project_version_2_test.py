# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 02:00:31 2022

@author: unimi
"""
from tensor import *

# for RGB images the chnnel = 3 and for Grayscale, the channel = 1

# The tensor named image_tenosr stores all the generated images, and it has 4 dimensions, [batch, channel, height, width ]


print(image_tensor.size())

# each elemnt of the the tensor "image_tensor" is an image in the form of a pytroch tensor, which has 3 dimensions [channel, height, width]

# it is possible to call the iamge numeber i, by writing image[i-1]

# For example image numeber 1:

img1 = image[0]

print(img1.size())

from torchvision.utils import save_image


# It is possible to demonstrate and save the image as png file.

# It shows each element of the pytorch tensor named image_tensor is an image.

save_image(img1, 'img1.png')


       
