#usage:python coupling2.py bcl rg1
# coding=utf-8
import os
import sys
import numpy as np
#rg1_name="./"+input("rg1_file:")
#bcl_name="./"+input("bcl_file:")
bcl_name="./"+sys.argv[1]
rg1_name="./"+sys.argv[2]
#see the rg1 file first
os.chdir(rg1_name)
rg1_files = os.listdir(os.getcwd())
print (rg1_files)
#then goto b850 file
os.chdir("../"+bcl_name)
bcl_files = os.listdir(os.getcwd())
print (bcl_files)
os.chdir("../")
num=0
coupling_file = open("coupling.dat",'w')
while num<50:
#遍历文件
	f_bcl = open(bcl_name+"/"+"bcl_"+str("%03d" % num)+'_h.log','r').readlines()
	ff_bcl = bcl_name+"/"+"bcl_"+str("%03d" % num)+'_h.log'
	print (ff_bcl)
	f_rg1 = open(rg1_name+"/"+"rg1_"+str("%03d" % num)+'.log','r').readlines()
	ff_rg1 = rg1_name+"/"+"rg1_"+str("%03d" % num)+'.log'
	print (ff_rg1)
#从logfile中得到bcl的偶极距ui和rg1的偶极距uj
	def find_dipole(ff):
		n = 0
		for i in ff:
			n += 1
			if "Dip. S." in i:
				break
		aa = ff[n].split()
		bb = [float(aa[1]),float(aa[2]),float(aa[3])]
		#print (bb)
		return bb
	dipole_bcl = find_dipole(f_bcl)
	dipole_rg1 = find_dipole(f_rg1)
#得到两分子片中心原子的坐标并计算中心距离和向量
	def find_atom(ff,nplus):
		n = 0
		for i in ff:
			if "Multiplicity" in i:
				break
			n += 1
		aa = ff[n+nplus].split()
		bb = [float(aa[1]),float(aa[2]),float(aa[3])]
		#print (bb)
		return bb
	center_bcl = find_atom(f_bcl,1)
	center_rg1 = find_atom(f_rg1,32)
	minus = np.array(center_bcl) - np.array(center_rg1)
	dis_bclrg1 = np.linalg.norm(minus)
	#print (dis_bclrg1)
	vector_bclrg1 = [minus[0],minus[1],minus[2]]
	#print (vector_bclrg1)
#代入公式计算得到耦合值 注意：计算的时候需要把距离的埃单位转化为au单位(后面那个转3个就行了，因为需要与上面的约分)，最后再把算得的总值转化为ev单位
	ang_au = 1.0/0.529177  #将ang单位转换为au单位:value*ang_au
	au_ev = 27.2116 #将au单位转换为ev:value*au_ev
	#print (dipole_bcl,dipole_rg1,vector_bclrg1)
	aa=3*(np.dot(dipole_bcl,vector_bclrg1))
	#print (aa)
	Vij_au = (np.dot(dipole_bcl,dipole_rg1))/(dis_bclrg1*ang_au)**3 - 3*(np.dot(dipole_bcl,vector_bclrg1))*(np.dot(dipole_rg1,vector_bclrg1))/((dis_bclrg1*ang_au)**3)/(np.dot(vector_bclrg1,vector_bclrg1))
	Vij = Vij_au*au_ev
	print (Vij)	
	coupling_file.write(str(Vij)+"\n")
	num+=1
coupling_file.close()
