#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 19:45:01 2020

@author: jarvis
"""
# Importing needed packages and tools
import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib.patches as patches 
import matplotlib as mpl
import numpy as np

# Using pandas to read the csv files and renaming the files to red_square
pd.read_csv('SquareProject.csv')
square_points = pd.read_csv('SquareProject.csv', delimiter=',')
red_square = np.matrix(square_points)
print(red_square)

# naming more variables to categorize the data points
x_points = np.zeros((4,1))
y_points = np.zeros((4,1))
vertical = np.zeros((4,1))
horizontal = np.zeros((4,1))

# Declaring variables to plot on an x and y coordinate
x_points[0,0] = red_square[0,0]
x_points[1,0] = red_square[1,0]
x_points[2,0] = red_square[2,0]
x_points[3,0] = red_square[3,0]

y_points[0,0] = red_square[0,1]
y_points[1,0] = red_square[1,1]
y_points[2,0] = red_square[2,1]
y_points[3,0] = red_square[3,1]

# Creating width and height of the red_square, and the origin points
width = abs(x_points[1,0]) + abs(x_points[3,0])
height = abs(y_points[1,0]) + abs(y_points[3,0])
lim = (-500,500)

origin_x = x_points[1,0]
origin_y = y_points[1,0]

# Plotting the red_square
figure1 = plt.figure()
ax = plt.gca()
red_square = patches.Rectangle((origin_x,origin_y), width, height, facecolor= 'red')
ax.add_patch(red_square)

# Declaring variables for transforming the blue square
v = float(input("How much would you like to move the square horizontally?:"))
h = float(input("How much would you like to move the square vertically?:"))
scale = float(input("How much to scale the square by?:"))
degrees = float(input("How much degrees to rotate the square by?:"))
print("\n")

rad = np.radians(degrees)
vertical = x_points+v
horizontal = y_points+h
width_2 = width*scale
height_2 = height*scale

origin_v= vertical[1,0]
origin_h= horizontal[1,0]

# Blue Square
blue_square = patches.Rectangle((origin_v,origin_h), width_2, height_2, facecolor= 'blue')

#declaring code for the rotation
rotation = mpl.transforms.Affine2D().rotate_deg(degrees) + ax.transData
blue_square.set_transform(rotation)

new_x = (horizontal*np.cos(rad) + vertical*np.sin(rad))
new_y = ((-1)*horizontal*np.sin(rad) + vertical*np.cos(rad))

ax.add_patch(blue_square)

plt.axis([-200,200,-200,200])
plt.show
blue_square= np.concatenate((vertical,horizontal), axis = 1)

print("The data for the second square is:")
print(blue_square)

# Recreating the new data points into a csv file
ind= [" "," "," "," "]
df= pd.DataFrame({"x":[blue_square[0,0], blue_square[1,0],blue_square[2,0],blue_square[3,0]]})
df.to_csv('BlueSquare_Data.csv')
