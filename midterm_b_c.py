"""
Created on Thu May  2 10:50:13 2019

@author: asus
"""

import numpy as np
import matplotlib.pyplot as plt
import os

 
mypath1 = os.getcwd() 
myairfoils = []
nvalux = []
nvaluy = []
xupper = []
yupper = []
xlower = []
ylower = []
camberline = []

for i,j,k in os.walk('.'):
    myairfoils = np.append(myairfoils,k)
    
data_list = np.random.choice(myairfoils,size = 100)

for airfoil in data_list:
        with open(airfoil) as f:
            lines = f.read().splitlines()
def plot (name,x,y):
    plt.figure(figsize= (8,6))
    plt.ylim(ymax=0.4)
    plt.ylim(ymin=-0.4)
    plt.plot(x,y, '--', label=name)
    plt.legend()
        
def chordline (x,y,leading_edge,trailing_edge): 
    plt.plot([0,1], [leading_edge, trailing_edge])
    return((leading_edge-trailing_edge)/(0-1))

def meancamber(x,y,xupper,yupper,ylower):
    camberlinee = [(yupper[i] + ylower[i])/2 for i in range(0,len(yupper))]
    plt.plot(xupper, camberlinee)
    return(camberlinee)

def maxthickness(x,y,xupper,yupper,ylower,xlower):
    t = [yupper[i] - ylower[i] for i in range(0,len(yupper))]
    ix = np.argmax(t)
    loca = xupper[ix]
    plt.plot([loca, loca], [y[ix], y[-ix]])
    return(ix)
    
def panels(name,x,y,xupper, yupper,xlower, ylower):
    plot(name,x,y)
    for i in range(0, len(xupper)):
        # upper
        plt.plot([xupper[i], xupper[i+1]], [yupper[i], yupper[i+1]],
                 '-o', color='g', alpha=1.0)
        upper_center = (xupper[i+1] + xupper[i])/2, (yupper[i+1] + yupper[i])/2
        slope1 = (yupper[i+1] - yupper[i])/(xupper[i+1] - xupper[i])
        ang1 = np.arctan(-1/slope1)
        if np.sin(ang1) >=0: 
            u,v = (np.cos(ang1), np.sin(ang1))  
        else: 
            u,v = (-np.cos(ang1), -np.sin(ang1))
        plt.quiver(upper_center[0], upper_center[1],u, v, color='purple', alpha=0.8)
        # lower
        plt.plot([xlower[i], xlower[i+1]], [ylower[i], ylower[i+1]],
                 '-o', color='g', alpha=1.0)
        lower_center = (xlower[i+1] + xlower[i])/2, (ylower[i+1] + ylower[i])/2
        slope2 = (ylower[i+1] - ylower[i])/(xlower[i+1] - xlower[i])
        ang2 = np.arctan(-1/slope_2)
        if np.sin(ang2) <=0: 
            u,v = (np.cos(ang2), np.sin(ang2))  
        else: 
            u,v = (-np.cos(ang2), -np.sin(ang2))
        plt.quiver(lower_center[0], lower_center[1],u, v, color='pink', alpha=0.8)  

def Type (x,y):
    slope1 = (y[0]-y[1])/(x[0]-x[1])
    slope2 = (y[-1]-y[-2])/(x[-1]-x[-2])
    ang = np.arctan(slope1) - np.arctan(slope2)
    if ang == 0:
        result = 'Cusped'
    else:
        result = 'Pointed'
    return(result)

for airfoil in data_list:
    fxy = np.loadtxt(airfoil, dtype = float)
    x_coor = fxy.T[0]
    y_coor = fxy.T[1]
    
    nvaluex, nvaluey = normalization(x_coor,y_coor)
    
    plot(airfoil,nvaluex,nvaluey)
    
    minimumx = np.argmin(nvaluex)
    xupper = new_x[:min_x]
    xlower = new_x[min_x : -1]
    yupper = new_y[:min_x]
    ylower = new_y[min_x : -1]
    
    leading_edge = nvaluey[np.argmin(nvaluex)]
    trailing_edge = nvaluey[np.argmax(nvaluex)]
    chordline(nvaluex,nvaluey,leading_edge,trailing_edge)
    meancamber(nvaluex,nvaluey,xupper,yupper,ylower)
    maxthickness(airfoil,nvaluex,nvaluey,xupper,yupper,ylower)
    panels(airfoil,nvalux,nvaluey,xupper, yupper,xlower, ylower)
    
    Type (nvaluex, nvaluey)
    
    plt.show()