
import matplotlib.pyplot as plt
import csv
import numpy as np

x1 = np.arange(0,51,10)
plt.xticks(x1)
#plt.xlim(0,5)
x=[]
y=[]

with open("rmsd2.dat","r") as csvfile:
    plots = csv.reader(csvfile,delimiter="	")
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))


plt.plot(x,y, label='rmsd',color='k')
plt.xlabel('Time(ns)')
plt.ylabel('rmsd(A)')
plt.title('RMSD of backbone atoms')
plt.legend()
plt.show()
