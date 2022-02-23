import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0,3,1000)
y1 = np.ones(1000)
y1[:] = 30
x2 = np.linspace(3,6,1000)
y2 = np.ones(1000)
y2[:] = 25
x3 = np.linspace(6,10,1000)
y3 = np.ones(1000)
y3[:] = 20

fig,ax = plt.subplots()
plt.plot(x1,y1,'r',linewidth = 4)
plt.axvline(x = 3, color = "black", linestyle = "--", ymin = 0, ymax = 1, label = "x = 3")
plt.plot(x2,y2,'b',linewidth = 4)
plt.axvline(x = 6, ymin = 0, ymax = 1,
            color ='black',linestyle = "--",label = "x = 6")
plt.plot(x3,y3,'g',linewidth = 4)
plt.xlim(-1,10)
plt.ylim(15,35)
plt.show()