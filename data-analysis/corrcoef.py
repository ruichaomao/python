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
a = str(raw_input("1:"))
b = str(raw_input("2:"))
data1 = read(a + '.dat')
data2 = read(b + '.dat')
a = np.array(data1)
b = np.array(data2)
#x = np.vstack((a,b))
p = np.corrcoef(a, b)
print ("result:")
print p
#q = np.corrcoef(x)
#print q

