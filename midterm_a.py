"""
Created on Thu May  2 10:25:55 2019

@author: asus
"""

mypath1 = os.getcwd() 
myairfoils = []

for i,j,k in os.walk('.'):
    myairfoils = np.append(myairfoils,k)
    
data_list = np.random.choice(myairfoils,size = 100)

for a_f in data_list:
        with open(a_f) as file:
            header = file.readline()
            x, y = np.loadtxt(file, dtype=float, unpack=True)  
    
        xlist, ylist = x.tolist(), y.tolist()  

        xlast,ylast = xlist[-1],ylist[-1]                           
        xlist.insert(0, xlast) 
        ylist.insert(0, ylast)                       
    
        x, y = np.array(xlist),  np.array(ylist)
        xarray , yarray = x.reshape(len(x),1), y.reshape(len(y),1)
        xy   = np.hstack((xarray, yarray))   
            
        plt.plot(x,y, '--')
        plt.title(header, loc='center')                
        plt.axes().set_aspect('equal')
        plt.ylim(ymax=0.4)
        plt.ylim(ymin=-0.4)
        plt.figure(figsize= (16,14))
        plt.show()