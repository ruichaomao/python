import os
import numpy as np
f_name="./"+raw_input("file:")
os.chdir(f_name)
os.mkdir("."+f_name+"_new")
files = os.listdir(os.getcwd())
#print (files)
for file in files:
    lines = open(file,'r').readlines()
    for eachline in lines:
        if "C1 " in eachline:
           # print (eachline)
            c1line = eachline.split()
            c1xyz = [float(c1line[6]),float(c1line[7]),float(c1line[8])]
        elif "C2 " in eachline:
            #print (eachline)
            c2line = eachline.split()
            c2xyz = [float(c2line[6]),float(c2line[7]),float(c2line[8])]
        else:
            continue
    d_beg = np.subtract(c1xyz,c2xyz)
    d_beg = np.linalg.norm(d_beg)

    hlink_x = (c1xyz[0]*(d_beg-1) + c2xyz[0])/d_beg
    hlink_y = (c1xyz[1]*(d_beg-1) + c2xyz[1])/d_beg
    hlink_z = (c1xyz[2]*(d_beg-1) + c2xyz[2])/d_beg

    newline="ATOM     46  H37 BCL X 586      "+str('%.3f'%hlink_x)+'  '+str('%.3f'%hlink_y)+'  '+str('%.3f'%hlink_z)+"  0.00  0.00\n"
   # print (newline)
    
    newlines = [newline if "C2 " in i else i for i in lines] 
#print (newlines)
    position = file.rfind(".")
    newname = file[:position]+"_h.pdb"
    newfile = open("."+f_name+"_new"+"/"+newname,'w')
    for eachline in newlines:
        newfile.write(eachline)
    newfile.close()
