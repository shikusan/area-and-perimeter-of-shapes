# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 16:08:05 2023

@author: chege
"""


while True:
    user_input= input('a.) Choose a shape  b.) exit ')
     
    if user_input.lower() == 'b':
        break
    shape= input('choose a shape (1.rectangle, 2.triangle, 3.circle): ')
    if shape=='1':
          l=float(input('Enter length of Rectangle'))
          w=float(input('Enter width of Rectangle'))
          Rp=abs(2*(l+w))
          print(f'Perimeter of the Rectangle is {Rp}')
        
    elif shape=='2':
          a=float(input('Enter first length of Triangle'))
          b=float(input('Enter second length of Triangle'))
          c=float(input('Enter third length of Triangle'))
          Tp=abs(a+b+c)
          print(f'Perimeter of the Triangle is {Tp}')
        
    elif shape=='3':
          r=float(input('Enter radius of circle'))
          Cp=abs(2*3.14*r)
          print(f'Perimeter of the Circle is {Cp}')
    
    else:
          print('Invalid shape choice. Please choose from "1.rectangle," "2.triangle," or "3.circle."')
          continue
    repeat=input('Do you want to calculate another shape? (Yes/No): ')
    if repeat.lower() == 'no':
        break
    
 
 
        
