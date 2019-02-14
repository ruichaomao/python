import numpy as np

def read(filename):
    data = []
    fp = open(filename, "r")
    line = fp.readline()
    while True:
        line = fp.readline()
        if line.strip() == "":
            break
        r = line.split()
        #if int(r[1]) == 1 or int(r[1]) == 2 or int(r[1]) == 3:
        data.append(float(r[1]))
    #print data
    fp.close()

    return data

data1 = read('869.dat')
data2 = read('870.dat')
a = np.array(data1)
b = np.array(data2)
#x = np.vstack((a,b))
p = np.corrcoef(a, b)
print ("result:")
print p
#q = np.corrcoef(x)
#print q
