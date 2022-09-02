# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 02:00:31 2022

@author: unimi
"""
from final_project import *

# for RGB images the chnnel = 3 and for Grayscale, the channel = 1

# The tensor named image_tenosr stores all the generated images, and it has 4 dimensions, [batch, channel, height, width ]


print(image_tensor.size())

# each elemnt of the the tensor "image_tensor" is an image in the form of a pytroch tensor, which has 3 dimensions [channel, height, width]

# it is possible to call the iamge numeber i, by writing image[i-1]

# For example image numeber 1:

img1 = image_tensor[0]

print(img1.size())

from torchvision.utils import save_image


# It is possible to demonstrate and save the image as png file.

# It shows each element of the pytorch tensor named image_tensor is an image.

save_image(img1, 'img1.png')

# Maybe it is needed to save the output pytorch as a file. https://pytorch.org/docs/stable/generated/torch.save.html

ask_to_save = input('Do you need to save the generated tensor as a file with .pt format, Write your answer with Yes or No? ')


if ask_to_save == 'Yes':
    name = input('Please write a desired name for the generated file: ' )
    torch.save(image_tensor , '{}.pt'.format(name))

       
