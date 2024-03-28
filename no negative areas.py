# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 11:06:30 2023

@author: chege
"""
print('Welcome to my area calculator!!!!!!')
print('*******************************')
print('For Area of Rectangle enter:R')
print('For Area of Triangle enter:T')
print('For Area of circle enter: C')
while True:
    shape= input('choose a shape (R, C, T): ')

    if shape.lower() =='r':
      l=abs(float(input('length')))
      w=abs(float(input('width')))
      areaR=l*w
      
      print(f'The area of the rectangle is {areaR}')

    elif shape.lower() == "c":
      r= abs(float(input('enter the radius of the circle')))
      areaC=3.14*(r**2)
      
      print(f"The area of th circle is {areaC}")

    elif shape.lower()=='t':
     b=float(input('base'))
     h=float(input('height'))
     areaT=(b*h)/2
     
     print(f'The area of the triangle is {abs(areaT)}')
    else: 
     print('Invalid shape choice. Please choose from "rectangle," "circle," or "triangle."')
    repeat = input('Do you want to calculate another shape? (Y/N): ')
    if repeat.lower() != 'y':
        break