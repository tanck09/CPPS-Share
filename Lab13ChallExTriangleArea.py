# -*- coding: utf-8 -*-
"""
Created on Wed May 20 10:04:05 2020

@author: tanck
"""
import math

def area(sideA,sideB,angle):
    """Calculate area of triangle  """
    result = 0.5* sideA * sideB * math.sin( math.radians(angle) )
    return result

def oppSide(sideA,sideB,angle):
    """Calculate opp sides of triangle  """
    result =  math.sqrt(sideA**2 + sideB**2  - 2* sideA * sideB * math.cos( math.radians(angle) ) )
    return result

side1 = 0.0
side2 = 0.0
angleC = 0.0

side1 = float (input("Enter side 1:"))
side2 = float (input("Enter side 2:"))
angleC =float (input("Enter the angle in degree:"))

calculatedArea = area (side1,side2, angleC) 
calculatedSide = oppSide(side1,side2, angleC) 
print (F"Area is {calculatedArea:.2f} ")
print (F"Opp side is {calculatedSide:.2f} ")
