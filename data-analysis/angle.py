import numpy as np
import os
os.chdir("./")
pw = os.getcwd()
print ("fdsfds")
filelist = [fina for fina in os.listdir(os.getcwd()) if fina.startswith("vect")]
for file in filelist:
    final_file = open(file+"2", "w+")
    ff = open(file, "r").readlines()
    fff = [i for i in ff if i != '\n']
    lenth = len(fff)
    print (lenth)
    num = 0
    while num < lenth:
        main_vect = fff[num].split("|")[0]
        l_vect = fff[num].split('|')[1]
        #print (type(main_vect),l_vect)
        mm = main_vect.strip().replace(" ",",").split(",")
        mmm = [float(i) for i in mm]
        ll = l_vect.strip().replace(" ",",").split(",")
        lll = [float(i) for i in ll]
        x = np.array(mmm)
        y = np.array(lll)
        #print (x,y)
        Lx = np.sqrt(x.dot(x))
        Ly = np.sqrt(y.dot(y))
        #print (Lx,Ly)
        cos_angle=x.dot(y)/(Lx*Ly)
        #print (cos_angle)
        angle = np.arccos(cos_angle)
        #print (angle)
        angle2 = angle*360/2/np.pi
        print (angle2)
        final_file.write(str(angle2)+"\n")
        num += 1
    final_file.close()

