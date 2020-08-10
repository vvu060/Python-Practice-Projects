import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

x = [0,1,2,3,4]
y = [0,2,4,6,8]
#print(plt.plot(x,y, label='2x', color='red', linewidth = 3, linestyle = '--', marker = '.', markersize = 10, markeredgecolor = 'yellow'))

#Resize the graph
plt.figure(figsize=(5,3), dpi=150)

#Use short hand notation
#fmt = [color][marker][line]
plt.plot(x,y, 'r*--',  label='2x')

#Line Number 2 using numpy
x2 = np.arange(0,4.5,0.5)
plt.plot(x2[:6], x2[:6]**2, 'b-',label = 'x^2')
plt.plot(x2[4:], x2[4:]**2, 'b--')             #[4:] to seperate line type


plt.title('My First Graph', fontdict={'fontname': 'calibri', 'fontsize': 20})
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.xticks([0,1,2,3,4])
#print(plt.yticks([0,2,4,6,8]))
plt.legend()
plt.savefig('F:/Python Codes/Pandas/mygraph.png')

plt.show()

















