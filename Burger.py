import matplotlib.pyplot as plt
import numpy as np

def convection(type_wave, nt, nx, tmax, xmax, c, amp=2.0):
    import ipywidgets as widgets
    import matplotlib.pyplot as plt
    import matplotlib.cm as cm
    import numpy as np
    from math import sqrt
    from math import ceil
    from math import exp
    from math import pi
    from math import sin
    # Increments
    dt = tmax / (nt)
    dx = xmax / (nx)
    x=np.zeros(nx)
    # Initialise data structures
    class Velocity:
        def __init__(self, type_wave, nt,nx):
            self.type = type_wave
            self.square=np.zeros((nx, nt))
            self.peak=np.zeros((nx, nt))
            self.exp=np.zeros((nx, nt))
            self.sine=np.zeros((nx, nt))
            
    u=Velocity(type_wave, nt, nx)          
   ###Creation of the initial situation
     
    #creation initial condition of square
    # Boundary conditions
    u.square[0, :] = u.square[nx-1, :] = 1
    # Initial conditions
    for i in range(1, nx - 1):
        if(i > 20 and i < 35):
            u.square[i,0] = amp
        else:
            u.square[i,0] = 1


    #creation initial condition of exp   
    # Boundary conditions
    u.exp[0, :] = u.exp[nx - 1, :] = 1
    # Initial conditions
    for i in range(1, nx - 1):
        u.exp[i, 0]=1+amp*exp(-30*(i*dx-0.5)**2)

    #creation initial condition of peak
   # Boundary conditions
    u.peak[0, :] = u.peak[nx - 1, :] = 1
    # Initial conditions
    for i in range(1, nx - 1):
        if (i > 25 and i <27):
            u.peak[i, 0] = amp
        else:
            u.peak[i, 0] = 1
            
   #creation initial condition of sine
   # Boundary conditions
    u.sine[0, :] = u.sine[nx - 1, :] = 1
    # Initial conditions
    for i in range(0, ceil(3*nx/4)):
        u.sine[i, 0]=1+amp/5*sin(i*dx*8*pi/(3*xmax))
    for i in range(ceil(3*nx/4), nx):
        u.sine[i, 0]=1

    ##Calculation of the evolution (time and space) of the initial condition    
    # Loop
    for n in range(0,nt-2):
        for i in range(1,nx-1):
            u.square[i,n+1] = u.square[i,n]-u.square[i,n]*(dt/dx)*(u.square[i,n]-u.square[i-1,n])
            u.exp[i,n+1] = u.exp[i,n]-u.exp[i,n]*(dt/dx)*(u.exp[i,n]-u.exp[i-1,n])
            u.peak[i,n+1] = u.peak[i,n]-u.peak[i,n]*(dt/dx)*(u.peak[i,n]-u.peak[i-1,n])
            u.sine[i,n+1] = u.sine[i,n]-u.sine[i,n]*(dt/dx)*(u.sine[i,n]-u.sine[i-1,n])
   # X Loop
    for i in range(0,nx):
        x[i]=i*dx
    return u,x


def plot_convection(type_wave,u,v,x, t=0):
    if type_wave =='square':
        fig, ax = plt.subplots()
        ax.cla()
        plt.plot(x,u.square[:,t],label='u (high amplitude)')
        plt.plot(x,v.square[:,t],label='v (low amplitude)')
        ax.legend()
        plt.ylim((-0.5,6+0.1))
    elif type_wave=='peak':
        fig, ax = plt.subplots()
        ax.cla()
        plt.plot(x,u.peak[:,t],label='u (high amplitude)')
        plt.plot(x,v.peak[:,t],label='v (low amplitude)')
        ax.legend()
        plt.ylim((-0.5,6+0.1))
    elif type_wave=='exp':
        fig, ax = plt.subplots()
        ax.cla()
        plt.plot(x,u.exp[:,t],label='u (high amplitude)')
        plt.plot(x,v.exp[:,t],label='v (low amplitude)')
        ax.legend()
        plt.ylim((-0.5,6+0.1))
    elif type_wave=='sine':
        fig, ax = plt.subplots()
        ax.cla()
        plt.plot(x,u.sine[:,t],label='u (high amplitude)')
        plt.plot(x,v.sine[:,t],label='v (low amplitude)')
        ax.legend()
        plt.ylim((-0.5,6+0.1))

def plot_convection_evol(type_wave,u,x, nt):
    import matplotlib.cm as cm
    if type_wave =='square':
        plt.figure(figsize=(20,10))
        colour=iter(cm.rainbow(np.linspace(0,30,nt)))
        for i in range(0,nt,20):
            c=next(colour)
            plt.plot(x,u.square[:,i],c=c)
            plt.xlabel('x (m)')
            plt.ylabel('u (m/s)')
            plt.ylim((-0.5,6+0.1))
            
    if type_wave =='peak':
        plt.figure(figsize=(20,10))
        colour=iter(cm.rainbow(np.linspace(0,30,nt)))
        for i in range(0,nt,20):
            c=next(colour)
            plt.plot(x,u.peak[:,i],c=c)
            plt.xlabel('x (m)')
            plt.ylabel('u (m/s)')
            plt.ylim((-0.5,6+0.1))
            
    elif type_wave=='exp':
        plt.figure(figsize=(20,10))
        colour=iter(cm.rainbow(np.linspace(0,30,nt)))
        for i in range(0,nt,20):
            c=next(colour)
            plt.plot(x,u.exp[:,i],c=c)
            plt.xlabel('x (m)')
            plt.ylabel('u (m/s)')
            plt.ylim((-0.5,6+0.1))
            
    elif type_wave=='sine':
        plt.figure(figsize=(20,10))
        colour=iter(cm.rainbow(np.linspace(0,30,nt)))
        for i in range(0,nt,30):
            c=next(colour)
            plt.plot(x,u.sine[:,i],c=c)
            plt.xlabel('x (m)')
            plt.ylabel('u (m/s)')
            plt.ylim((-0.5,6+0.1))
            
def plot_convection_evol_3d(type_wave,u,x, nt):    
    import matplotlib.cm as cm
    from mpl_toolkits.mplot3d import Axes3D
    if type_wave =='square':
        plt.figure()
        ax = plt.subplot(projection='3d')
        colour=iter(cm.rainbow(np.linspace(0,30,nt)))
        for i in range(0,nt,20):    
            c=next(colour)
            ax.plot(x, u.square[:, i], i, c=c)

     
    elif type_wave =='exp':
        plt.figure()
        ax = plt.subplot(projection='3d')
        colour=iter(cm.rainbow(np.linspace(0,30,nt)))
        for i in range(0,nt,20):    
            c=next(colour)
            ax.plot(x, u.exp[:, i], i, c=c)
            
    elif type_wave =='peak':
        plt.figure()
        ax = plt.subplot(projection='3d')
        colour=iter(cm.rainbow(np.linspace(0,30,nt)))
        for i in range(0,nt,20):    
            c=next(colour)
            ax.plot(x, u.peak[:, i], i, c=c)
            
    elif type_wave =='sine':
        plt.figure()
        ax = plt.subplot(projection='3d')
        colour=iter(cm.rainbow(np.linspace(0,30,nt)))
        for i in range(0,nt,20):    
            c=next(colour)
            ax.plot(x, u.sine[:, i], i, c=c)





def convection_visc(type_wave, nt, nx, tmax, xmax, c, amp, nu=0.1):
    import ipywidgets as widgets
    import matplotlib.pyplot as plt
    import matplotlib.cm as cm
    import numpy as np
    from math import sqrt
    from math import ceil
    from math import exp
    from math import pi
    from math import sin
    # Increments
    dt = tmax / (nt)
    dx = xmax / (nx)
    x=np.zeros(nx)
    # Initialise data structures
    class Velocity:
        def __init__(self, type_wave, nt,nx):
            self.type = type_wave
            self.square=np.zeros((nx, nt))
            self.peak=np.zeros((nx, nt))
            self.exp=np.zeros((nx, nt))
            self.square_visc=np.zeros((nx, nt))
            self.peak_visc=np.zeros((nx, nt))
            self.exp_visc=np.zeros((nx, nt))
            self.sine=np.zeros((nx, nt))
            self.sine_visc=np.zeros((nx, nt))
            
    u=Velocity(type_wave, nt, nx)   
    
    #square
    # Boundary conditions
    u.square[0, :] = u.square[nx-1, :] = 1
    # Initial conditions
    for i in range(1, nx - 1):
        if(i > 10 and i < 20):
            u.square[i,0] = amp
        else:
            u.square[i,0] = 1

    u.square_visc[:,:]=u.square[:,:]
    
    
    #exp   
    # Boundary conditions
    u.exp[0, :] = u.exp[nx - 1, :] = 1
    # Initial conditions
    for i in range(1, nx - 1):
        u.exp[i, 0]=1+amp*exp(-30*(i*dx-0.5)**2)
    u.exp_visc[:,:]=u.exp[:,:]
    
    
    #peak
   # Boundary conditions
    u.peak[0, :] = u.peak[nx - 1, :] = 1
    # Initial conditions
    for i in range(1, nx - 1):
        if (i > 25 and i <27):
            u.peak[i, 0] = amp
        else:
            u.peak[i, 0] = 1
    u.peak_visc[:,:]=u.peak[:,:]
    
    #sine
      # Boundary conditions
    u.sine[0, :] = u.sine[nx - 1, :] = 1
    # Initial conditions
    for i in range(0, ceil(3*nx/4)):
        u.sine[i, 0]=1+amp/5*sin(i*dx*8*pi/(3*xmax))
    for i in range(ceil(3*nx/4), nx):
        u.sine[i, 0]=1
    u.sine_visc[:,:]=u.sine[:,:]

    # Loop
    for n in range(0,nt-2):
        for i in range(1,nx-1):
            u.square[i,n+1] = u.square[i,n]-u.square[i,n]*(dt/dx)*(u.square[i,n]-u.square[i-1,n])
            u.exp[i,n+1] = u.exp[i,n]-u.exp[i,n]*(dt/dx)*(u.exp[i,n]-u.exp[i-1,n])
            u.peak[i,n+1] = u.peak[i,n]-u.peak[i,n]*(dt/dx)*(u.peak[i,n]-u.peak[i-1,n])
            u.sine[i,n+1] = u.sine[i,n]-u.sine[i,n]*(dt/dx)*(u.sine[i,n]-u.sine[i-1,n])

            u.square_visc[i,n+1] = u.square_visc[i,n]-u.square_visc[i,n]*(dt/dx)*(u.square_visc[i,n]-u.square_visc[i-1,n])+nu*(dt/(dx*dx))*(u.square_visc[i+1,n]-2*u.square_visc[i,n]+u.square_visc[i-1,n])
            u.sine_visc[i,n+1] = u.sine_visc[i,n]-u.sine_visc[i,n]*(dt/dx)*(u.sine_visc[i,n]-u.sine_visc[i-1,n])+nu*(dt/(dx*dx))*(u.sine_visc[i+1,n]-2*u.sine_visc[i,n]+u.sine_visc[i-1,n])
            u.peak_visc[i,n+1] = u.peak_visc[i,n]-u.peak_visc[i,n]*(dt/dx)*(u.peak_visc[i,n]-u.peak_visc[i-1,n])+nu*(dt/(dx*dx))*(u.peak_visc[i+1,n]-2*u.peak_visc[i,n]+u.peak_visc[i-1,n])
            u.exp_visc[i,n+1] = u.exp_visc[i,n]-u.exp_visc[i,n]*(dt/dx)*(u.exp_visc[i,n]-u.exp_visc[i-1,n])+nu*(dt/(dx*dx))*(u.exp_visc[i+1,n]-2*u.exp_visc[i,n]+u.exp_visc[i-1,n])
            
            
   # X Loop
    for i in range(0,nx):
        x[i]=i*dx
    
    return u,x
def plot_convection_visc(type_wave,u,v,x, t=0):
    if type_wave =='square':
        fig, ax = plt.subplots()
        #ax.cla()
        plt.plot(x,u.square[:,t],label='u (high amplitude), no viscosity')
        plt.plot(x,v.square[:,t],label='v (low amplitude), no viscosity')
        plt.plot(x,u.square_visc[:,t],label='u (high amplitude), with viscosity')
        plt.plot(x,v.square_visc[:,t],label='v (low amplitude), with viscosity')
        ax.legend()
        plt.ylim((-0.5,6+0.1))
    elif type_wave=='peak':
        fig, ax = plt.subplots()
        #ax.cla()
        plt.plot(x,u.peak[:,t],label='u (high amplitude), no viscosity')
        plt.plot(x,v.peak[:,t],label='v (low amplitude), no viscosity')
        plt.plot(x,u.peak_visc[:,t],label='u (high amplitude), with viscosity')
        plt.plot(x,v.peak_visc[:,t],label='v (low amplitude), with viscosity')
        ax.legend()
        plt.ylim((-0.5,6+0.1))
    elif type_wave=='exp':
        fig, ax = plt.subplots()
        #ax.cla()
        plt.plot(x,u.exp[:,t],label='u (high amplitude), no viscosity')
        plt.plot(x,v.exp[:,t],label='v (low amplitude), no viscosity')
        plt.plot(x,u.exp_visc[:,t],label='u (high amplitude), with viscosity')
        plt.plot(x,v.exp_visc[:,t],label='v (low amplitude), with viscosity')
        ax.legend()
        plt.ylim((-0.5,6+0.1))
    elif type_wave=='sine':
        fig, ax = plt.subplots()
        #ax.cla()
        plt.plot(x,u.sine[:,t],label='u (high amplitude), no viscosity')
        plt.plot(x,v.sine[:,t],label='v (low amplitude), no viscosity')
        plt.plot(x,u.sine_visc[:,t],label='u (high amplitude), with viscosity')
        plt.plot(x,v.sine_visc[:,t],label='v (low amplitude), with viscosity')
        ax.legend()
        plt.ylim((-0.5,6+0.1))
        
        
def plot_log():
    rho=np.arange(1.0,50.0,0.1)
    v=27.5*np.log(142/rho)
    fig, ax = plt.subplots(figsize=(20,10))
    #ax.cla()
    plt.plot(rho,v,label='Velocity due the density of car')
    ax.legend()
    plt.xlabel('density of the cars on the road [cars/km]')
    plt.ylabel('Mean velocity of the cars [km/hr]')
    plt.xlim((0,50))
    
    
def convection2(type_wave, nt, nx, tmax, xmax, c, amp=2):
    import numpy as np
    from math import sqrt
    from math import ceil
    from math import exp
    from math import pi
    from math import sin
    # Increments
    dt = tmax / (nt)
    dx = xmax / (nx)
    x=np.zeros(nx)
    # Initialise data structures                
    class amp:
        def __init__(self):
            self.amp2 = 2
            self.amp3 = 3
            self.amp4 = 4
            self.amp5 = 5
            self.amp6 = 6
            self.amp7 = 7
    class Type:
        def __init__(self,type_wave, nt, nx, amp):
            self.type = type_wave
            self.data = amp
            self.square = np.zeros((nx, nt))
            self.peak = np.zeros((nx, nt))
            self.exp = np.zeros((nx, nt))
            self.sine = np.zeros((nx, nt))

            
    u=amp()
    u.amp2=Type(type_wave, nt, nx, amp)                
    u.amp3=Type(type_wave, nt, nx, amp)
    u.amp4=Type(type_wave, nt, nx, amp)                
    u.amp5=Type(type_wave, nt, nx, amp)
    u.amp6=Type(type_wave, nt, nx, amp)                
    u.amp7=Type(type_wave, nt, nx, amp)
    
    def initialcond(u, nt, nx, amp):
        from math import sqrt
        from math import ceil
        from math import exp
        from math import pi
        from math import sin
        
        ###Creation of the initial situation

        #creation initial condition of square
        # Boundary conditions
        u.square[0, :] = u.square[nx-1, :] = 1
        # Initial conditions
        for i in range(1, nx - 1):
            if(i > 20 and i < 35):
                u.square[i,0] = amp
            else:
                u.square[i,0] = 1


        #creation initial condition of exp   
        # Boundary conditions
        u.exp[0, :] = u.exp[nx - 1, :] = 1
        # Initial conditions
        for i in range(1, nx - 1):
            u.exp[i, 0]=1+amp*exp(-30*(i*dx-0.5)**2)

        #creation initial condition of peak
       # Boundary conditions
        u.peak[0, :] = u.peak[nx - 1, :] = 1
        # Initial conditions
        for i in range(1, nx - 1):
            if (i > 25 and i <27):
                u.peak[i, 0] = amp
            else:
                u.peak[i, 0] = 1

       #creation initial condition of sine
       # Boundary conditions
        u.sine[0, :] = u.sine[nx - 1, :] = 1
        # Initial conditions
        for i in range(0, ceil(3*nx/4)):
            u.sine[i, 0]=1+amp/7*sin(i*dx*8*pi/(3*xmax))
        for i in range(ceil(3*nx/4), nx):
            u.sine[i, 0]=1

        ##Calculation of the evolution (time and space) of the initial condition    
        # Loop
        for n in range(0,nt-2):
            for i in range(1,nx-1):
                u.square[i,n+1] = u.square[i,n]-u.square[i,n]*(dt/dx)*(u.square[i,n]-u.square[i-1,n])
                u.exp[i,n+1] = u.exp[i,n]-u.exp[i,n]*(dt/dx)*(u.exp[i,n]-u.exp[i-1,n])
                u.peak[i,n+1] = u.peak[i,n]-u.peak[i,n]*(dt/dx)*(u.peak[i,n]-u.peak[i-1,n])
                u.sine[i,n+1] = u.sine[i,n]-u.sine[i,n]*(dt/dx)*(u.sine[i,n]-u.sine[i-1,n])
      
        return u
   

    u.amp2 = initialcond(u.amp2, nt, nx, 2)
    u.amp3 = initialcond(u.amp3, nt, nx, 3)
    u.amp4 = initialcond(u.amp4, nt, nx, 4)
    u.amp5 = initialcond(u.amp5, nt, nx, 5)
    u.amp6 = initialcond(u.amp6, nt, nx, 6)
    u.amp7 = initialcond(u.amp7, nt, nx, 7)

    # X Loop
    for i in range(0,nx):
        x[i]=i*dx       
    
    return u, x

def plot_color(u,x, nt):
    import matplotlib.cm as cm
    plt.figure(figsize=(20,10))
    colour=iter(cm.rainbow(np.linspace(0,30,nt)))
    for i in range(0,nt,20):
        c=next(colour)
        plt.plot(x,u[:,i],c=c)
        plt.xlabel('x (m)')
        plt.ylabel('u (m/s)')
        plt.ylim((-0.5,7+0.1))
