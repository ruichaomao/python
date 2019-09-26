#coding=utf-8
import os
#change the dir
f_name="./"+raw_input("file:")
os.chdir(f_name)
os.mkdir("."+f_name+"_new")
files = os.listdir(os.getcwd())
print (files)
for file in files:
    f = open (file,"r")
    lines = f.readlines()
    f.close()
    position = file.rfind(".")
    newname = file[:position]+".mop"
    ff = open ("."+f_name+"_new"+"/"+newname,"w")
    #keyword
    ff.seek(0,0)
    ff.write("PM7 1SCF VECTORS NOGPU times AUX threads=14\ndescription\ndescription2\n") 
    for line in lines:
        if "ATOM" in line:
            line=line.strip()
            aa = line[12:16].strip()
            if aa == "MG":
                ff.write(aa+(" ")*10+line[31:55])
            else:
                ff.write(" "+aa[0]+(" ")*10+line[31:55])
        else:
            continue
        ff.write("\n")
ff.close()
