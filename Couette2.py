import matplotlib.pyplot as plt
import numpy as np
from math import *

def plot_img(name_image):
    import matplotlib.image as mpimg
    image = mpimg.imread(name_image)
    plt.figure(figsize=(20,10))
    plt.imshow(image)
    plt.axis('off')
    plt.show()
    
    

def solve_vel_couette(v_0=10.0, h=8./3, x0=0):
    x=[]
    y=[]
    for i in np.arange(0.0, h, 0.5):
        x=np.append(x,v_0*i/h)
        y=np.append(y,i)
    n=0
    v_max=v_0
    
    plt.figure(figsize=(20,10))
    if v_0>0:
        for i in range(len(np.arange(0.0, h, 0.5))-1):
            plt.arrow(x0, y[i+1], x[i+1]-0.5, 0, head_width=0.5)
            n+=1
    if v_0<0:
        for i in range(len(np.arange(0.0, h, 0.5))-1):
            plt.arrow(x0, y[i+1], x[i+1]+0.5, 0, head_width=0.5)
            n+=1
    # prepare the axes limits
    plt.ylim((-1.5,11))
    plt.xlim((0,60))
    
    plt.plot([x0,x0+x[n]*h/y[n]],[0,h], color='k', linestyle='-')
    plt.plot([x0,x0],[0,h], color='k', linestyle='-')
    
    plt.axhline(y=h, color='r', linestyle='-')
    s="Upper moving plate"
    k="x0"
    plt.text(15, h+0.5, s, fontdict=None, withdash=False)
    plt.text(x0, -0.5, k, fontdict=None, withdash=False)
    
    plt.axhline(y=0, color='b', linestyle='-')
    t="Lower fixed plate"
    plt.text(15, -1, t, fontdict=None, withdash=False)
    plt.grid()
    plt.show()
    
    
def solve_vel_pois(h=8./3,x0=0, delta_p=0, nu=4):
    x=[]
    y=[]
    v_max=-h**2/(8*nu)*(delta_p) 
    for i in np.arange(0.0, h, 0.5):
        x=np.append(x,v_max*(4*i/h-4*(i**2)/(h**2)))
        y=np.append(y,i)
    n=0
    plt.figure(figsize=(20,10))
    if delta_p>0:
        for i in range(len(np.arange(0.0, h, 0.5))-1):
            plt.arrow(x0, y[i+1], x[i+1], 0, head_width=0.5)
            if (x[i]<0) and (x[i+1]<0):
                plt.plot([x0+x[i]-0.5, x0+x[i+1]-0.5], [y[i],y[i+1]], color='k', linestyle='-')
            elif (x[i]>0)and(x[i+1]>0):
                plt.plot([x0+x[i], x0+x[i+1]], [y[i],y[i+1]], color='k', linestyle='-')
            n+=1
        if (x[i]<=0) and (x[i+1]<=0):
            plt.plot([x0+x[len(np.arange(0.0, h, 0.5))-1]-0.5, x0], [y[len(np.arange(0.0, h, 0.5))-1],h], color='k', linestyle='-')
            plt.plot([x0, x0+x[1]-0.5], [0,y[1]], color='k', linestyle='-')
        elif (x[i]>=0) and (x[i+1]>=0):
            plt.plot([x0+x[len(np.arange(0.0, h, 0.5))-0.5], x0], [y[len(np.arange(0.0, h, 0.5))-1],h], color='k', linestyle='-')
            plt.plot([x0, x0+x[1]-0.5], [0,y[1]], color='k', linestyle='-')
            
    if delta_p<0:
        for i in range(len(np.arange(0.0, h, 0.5))-1):
            plt.arrow(x0, y[i+1], x[i+1], 0, head_width=0.5)
            if (x[i]<0) and (x[i+1]<0):
                plt.plot([x0+x[i], x0+x[i+1]], [y[i],y[i+1]], color='k', linestyle='-')
            elif (x[i]>0)and(x[i+1]>0):
                plt.plot([x0+x[i]+0.5, x0+x[i+1]+0.5], [y[i],y[i+1]], color='k', linestyle='-')
            n+=1
            
        if (x[i]<=0) and (x[i+1]<=0):
            plt.plot([x0+x[len(np.arange(0.0, h, 0.5))-1]-0.5, x0], [y[len(np.arange(0.0, h, 0.5))-1],h], color='k', linestyle='-')
            plt.plot([x0, x0+x[1]-1], [0,y[1]], color='k', linestyle='-')
        elif (x[i]>=0) and (x[i+1]>=0):
            plt.plot([x0+x[len(np.arange(0.0, h, 0.5))-1]+0.5, x0], [y[len(np.arange(0.0, h, 0.5))-1],h], color='k', linestyle='-')
            plt.plot([x0, x0+x[1]+0.5], [0,y[1]], color='k', linestyle='-')
    if delta_p==0:
        plt.plot([x0, x0], [0,h], color='k', linestyle='-')
    # prepare the axes limits
    plt.ylim((-1.5,13))
    plt.xlim((0,60))
      
    #plt.plot([x0,x0+x[n]*h/y[n]],[0,h], color='k', linestyle='-')
    plt.plot([x0,x0],[0,h], color='k', linestyle='-')
    
    plt.axhline(y=h, color='r', linestyle='-')
    s="Upper fixed plate"
    k="x0"
    plt.text(15, h+0.5, s, fontdict=None, withdash=False)
    plt.text(x0, -0.5, k, fontdict=None, withdash=False)
    text="vmax=%.2f" % round(v_max,2)

    plt.text(40, 12, text, fontdict=None, withdash=False)
    
    t_p1="p1"
    t_p2="p2"
    
    plt.text(2, h/2, t_p1, fontdict=None, withdash=False)
    plt.text(57, h/2, t_p2, fontdict=None, withdash=False)
    
    plt.axhline(y=0, color='b', linestyle='-')
    t="Lower fixed plate"
    plt.text(15, -1, t, fontdict=None, withdash=False)
    plt.grid()
    plt.show()
    
def solve_vel_couette_pois(v_0=10.0, h=8./3, x0=0, delta_p=0, nu=4):
    
    x=[]
    y=[]
    v_max1=-h**2/(8*nu)*(delta_p)
    v_max2=v_0
    for i in np.arange(0.0, h, 0.5):
        x=np.append(x,v_max1*(4*i/h-4*(i**2)/(h**2))+v_0*i/h)
        y=np.append(y,i)
    n=0
    
    plt.figure(figsize=(20,10))
    for i in range(len(np.arange(0.0, h, 0.5))-1):
        # plt.plot([x0,x0+x[n]*h/y[n]],[0,h], color='k', linestyle='-')
        plt.arrow(x0, y[i+1], x[i+1], 0, head_width=0.5)
        if (x[i])<0 and (x[i+1])<0:
            plt.plot([x0+x[i]-0.5, x0+x[i+1]-0.5], [y[i],y[i+1]], color='k', linestyle='-')
        elif (x[i])==0 and (x[i+1])==0:
            plt.plot([x0+x[i], x0+x[i+1]], [y[i],y[i+1]], color='k', linestyle='-')
        elif (x[i])==0 and (x[i+1])<0:
            plt.plot([x0+x[i], x0+x[i+1]-0.5], [y[i],y[i+1]], color='k', linestyle='-')
        elif (x[i])<0 and (x[i+1])==0:
            plt.plot([x0+x[i]-0.5, x0+x[i+1]], [y[i],y[i+1]], color='k', linestyle='-')
        
        elif (x[i])<0 and (x[i+1])>0:
            plt.plot([x0+x[i]-0.5, x0+x[i+1]+0.5], [y[i],y[i+1]], color='k', linestyle='-')
        elif (x[i])>0 and (x[i+1])<0:
            plt.plot([x0+x[i]+0.5, x0+x[i+1]-0.5], [y[i],y[i+1]], color='k', linestyle='-')
        
        elif (x[i])>0and(x[i+1])==0:
            plt.plot([x0+x[i]+1, x0+x[i+1]], [y[i],y[i+1]], color='k', linestyle='-')
        elif (x[i])==0and(x[i+1])>0:
            plt.plot([x0+x[i], x0+x[i+1]+0.5], [y[i],y[i+1]], color='k', linestyle='-')
        elif (x[i])>0and(x[i+1])>0:
            plt.plot([x0+x[i]+0.5, x0+x[i+1]+0.5], [y[i],y[i+1]], color='k', linestyle='-')
        n+=1
    
    
    
    
    
    
    
    
    
    
    
    
    if v_0>0 and x[len(np.arange(0.0, h, 0.5))-1]>0:
        plt.plot([x0+x[len(np.arange(0.0, h, 0.5))-1]+0.5, x0+v_0], [y[len(np.arange(0.0, h, 0.5))-1],h], color='k', linestyle='-')
    elif v_0>0 and x[len(np.arange(0.0, h, 0.5))-1]<0:
        plt.plot([x0+x[len(np.arange(0.0, h, 0.5))-1]-0.5, x0+v_0], [y[len(np.arange(0.0, h, 0.5))-1],h], color='k', linestyle='-')
    elif v_0==0 and x[len(np.arange(0.0, h, 0.5))-1]<0:
        plt.plot([x0+x[len(np.arange(0.0, h, 0.5))-1]-0.5, x0+v_0], [y[len(np.arange(0.0, h, 0.5))-1],h], color='k', linestyle='-')
    elif v_0==0 and x[len(np.arange(0.0, h, 0.5))-1]>0:
        plt.plot([x0+x[len(np.arange(0.0, h, 0.5))-1]+0.5, x0+v_0], [y[len(np.arange(0.0, h, 0.5))-1],h], color='k', linestyle='-')
    elif v_0<0 and x[len(np.arange(0.0, h, 0.5))-1]<0:
        plt.plot([x0+x[len(np.arange(0.0, h, 0.5))-1]-0.5, x0+v_0], [y[len(np.arange(0.0, h, 0.5))-1],h], color='k', linestyle='-')
    elif v_0<0 and x[len(np.arange(0.0, h, 0.5))-1]>0:
        plt.plot([x0+x[len(np.arange(0.0, h, 0.5))-1]+0.5, x0+v_0], [y[len(np.arange(0.0, h, 0.5))-1],h], color='k', linestyle='-')
    #plt.plot([x0, x0+x[1]], [0,y[1]], color='k', linestyle='-')
    # prepare the axes limits
    plt.ylim((-1.5,13))
    plt.xlim((0,60))
      
    #plt.plot([x0,x0+x[n]*h/y[n]],[0,h], color='k', linestyle='-')
    plt.plot([x0,x0],[0,h], color='k', linestyle='-')
    
    plt.axhline(y=h, color='r', linestyle='-')
    s="Upper moving plate"
    k="x0"
    plt.text(15, h+0.5, s, fontdict=None, withdash=False)
    plt.text(x0, -0.5, k, fontdict=None, withdash=False)
    
    t_p1="p1"
    t_p2="p2"
    
    plt.text(2, h/2, t_p1, fontdict=None, withdash=False)
    plt.text(57, h/2, t_p2, fontdict=None, withdash=False)
    
    plt.axhline(y=0, color='b', linestyle='-')
    t="Lower fixed plate"
    plt.text(15, -1, t, fontdict=None, withdash=False)
    
    """text="vmax=%.2f" % max(x)
    plt.text(40, 12, text, fontdict=None, withdash=False)"""
    plt.grid()
    plt.show()
        
