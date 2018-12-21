#coding=utf-8
#maoruichao 2018-12-21
#Convert pdb in amber format to pdb in charmm format, then generate psf and crd for charmm
#Command:  python trans_amber_charmm.py -i input.pdb
# run
# ./trans_amber_charmm.py -h
# for help
import re
import sys
sys.path.append('/home3/maoruichao/dynamics/charmm/test_script/test5_oop/pack')
import argparse
parser = argparse.ArgumentParser(
	description='this is a program which trans amber_pdb to charmm_pdb,then generate the charmm psf,crd,and pdb',
	formatter_class=argparse.RawTextHelpFormatter
	)
parser.add_argument('-i', '--input', help='Input PDB file')
parser.add_argument('-v', '--version', action='version', version='v. 1.0')
args = parser.parse_args()

#1/fold-judge:Determine if the folder exists, if it does not exist, create it
print ('{0}\nFirst, check if the required folder exists...'.format(50*'-'))
from mk_fold import  foldjudge
fold1 = foldjudge(['prot','ligand','popwat','output'])
fold1.mkdir_fold()
print ('{0}\nThe required folder has been created,\nnow the work of protein begins...'.format(50*'-'))
#2/protein-processing:截取蛋白，删除带有ACE的行，然后把HIE换成HSE,然后残基名amber转charmm,然后每个链保存为一个文件
#loadin trans_rsn-module
from trans_rsn import  trans_rs
lines = open(args.input,'r').readlines()
list_pro = []
for eachline in lines:
	if "BCL" not in eachline:
		list_pro.append(eachline)
	else:
		list_pro.append('END\n')
		break
list2_pro = [row.strip() for row in list_pro if 'ACE' not in row]
list3_pro = [row.replace('HIE','HSE') for row in list2_pro]
with open("testout.pdb",'w') as ff:
	a = [ff.write(row+'\n') for row in list3_pro]
ff.close() 
#use trans_rsn-module
pdb1 = trans_rs('testout.pdb')
pdb1.cont = pdb1.trans_file()
ff = open('testout2.pdb','w')
for line in pdb1.cont:
	ff.write(line+'\n')
ff.close()
#divide
ff = open('testout2.pdb')
line_list = ff.readlines()
ff.close()
new_list=[]
n = 1
for line in line_list:
	if 'OXT' not in line:
		new_list.append(line)
	else:
		new_list.append(line)
		new_list.append('END'+'\n')
		filename = './prot/prot'+str(n)+'.pdb'
		ff = open(filename,'w')
		for line in new_list:
			ff.write(line)
		ff.close()
		new_list=[]
		n+=1
		continue
print ('{0}\nEnd of work of protein,\nnow the work of ligand begins...'.format(50*'-'))
#3/ligand-processing:分别取出BCL和RG1和Cl-,保存为三个文件，然后分别将残基编号排序
#import trans_rsn-module
from renumber import  trans
lines = open(args.input,'r').readlines()
#RG1
list_rg1 = []
for eachline in lines:
	if "RG1" in eachline:
		list_rg1.append(eachline)
	else:
		continue
list_rg1.append("END\n")
ff = open("./ligand/rg1_all.pdb",'w')
for eachline in list_rg1:
	ff.write(eachline)
ff.close()
pdb1 = trans("./ligand/rg1_all.pdb")
pdb1.cont = pdb1.renumber_residues()
pdb1.cont = pdb1.renumber_atoms()
ff = open('./ligand/rg1_all_renum.pdb','w')
for line in pdb1.cont:
	ff.write(line+'\n')
ff.close()
#BCL
list_bcl = []
for eachline in lines:
	if "BCL" in eachline:
		list_bcl.append(eachline)
	else:
		continue
list_bcl.append("END\n")
ff = open("./ligand/bcl_all.pdb",'w')
for eachline in list_bcl:
	ff.write(eachline)
ff.close()
pdb1 = trans("./ligand/bcl_all.pdb")
pdb1.cont = pdb1.renumber_residues()
pdb1.cont = pdb1.renumber_atoms()
ff = open('./ligand/bcl_all_renum.pdb','w')
for line in pdb1.cont:
	ff.write(line+'\n')
ff.close()
#Cl-
list_cl = []
for eachline in lines:
	if "Cl-" in eachline:
		list_cl.append(eachline)
	else:
		continue
list_cl.append("END\n")
ff = open("./ligand/cl.pdb",'w')
for eachline in list_cl:
	ff.write(eachline)
ff.close()
print ('{0}\nEnd of work of ligand,\nnow the work of POP begins...'.format(50*'-'))
#4/lipid-processing:取出POP,并将POP改为POPC,保存为pdb
list_popc = []
for eachline in lines:
	if "POP" in eachline:
		line = eachline.replace('POP ','POPC')
		list_popc.append(line)
	else:
		continue
list_popc.append("END\n")
ff = open("./popwat/popc.pdb",'w')
for eachline in list_popc:
	ff.write(eachline)
ff.close()
print ('{0}\nEnd of work of POP,\nnow the work of water begins...'.format(50*'-'))
#5/water-pcocessing:取出WAT,修改为charmm格式，将水分子分成四片，并排序+修改格式是的编号可读
########将水分子分片##################################
#wat
list_wat = []
for eachline in lines:
	if "WAT" in eachline:
		line = eachline.replace('WAT ','TIP3').replace('O   TIP3','OH2 TIP3')
		list_wat.append(line)
	else:
		continue
list_wat.append("END\n")
ff = open("./popwat/wat.pdb",'w')
for eachline in list_wat:
	ff.write(eachline)
ff.close()
##wat1
lines = open('./popwat/wat.pdb','r').readlines()
list_wat1 = []
for eachline in lines:
	if "ATOM  93667" not in eachline:
		list_wat1.append(eachline)
	else:
		break
list_wat1.append("END\n")
ff = open("./popwat/wat1.pdb",'w')
for eachline in list_wat1:
	ff.write(eachline)
ff.close()
#use renumber module
pdb1 = trans("./popwat/wat1.pdb")
pdb1.cont = pdb1.renumber_residues()
pdb1.cont = pdb1.renumber_atoms()
ff = open("./popwat/wat1_renum.pdb",'w')
for line in pdb1.cont:
	ff.write(line+'\n')
ff.close()

#修改格式使得残基编号可读
lines = open('./popwat/wat1_renum.pdb','r').readlines()
list_wat1_final=[]
for eachline in lines:
	line = re.sub('X.',' ',eachline)
	list_wat1_final.append(line)
ff = open("./popwat/wat1_renum_modi.pdb",'w')
for eachline in list_wat1_final:
	ff.write(eachline)
ff.close()
	
#wat2
lines = open('./popwat/wat.pdb','r').readlines()
list_wat2 = []
a = True
for eachline in lines:
	if a and ("ATOM  93667" not in eachline):
		continue
	elif 'ATOM  1e310' in eachline:
		break
	else:
		a = False
		list_wat2.append(eachline)
list_wat2.append("END\n")
ff = open("./popwat/wat2.pdb",'w')
for eachline in list_wat2:
	ff.write(eachline)
ff.close()
pdb1 = trans("./popwat/wat2.pdb")
pdb1.cont = pdb1.renumber_residues()
pdb1.cont = pdb1.renumber_atoms()
ff = open("./popwat/wat2_renum.pdb",'w')
for line in pdb1.cont:
	ff.write(line+'\n')
ff.close()

#修改格式使得残基编号可读
lines = open('./popwat/wat2_renum.pdb','r').readlines()
list_wat2_final=[]
for eachline in lines:
	line = re.sub('X.',' ',eachline)
	list_wat2_final.append(line)
ff = open("./popwat/wat2_renum_modi.pdb",'w')
for eachline in list_wat2_final:
	ff.write(eachline)
ff.close()

#wat3
lines = open('./popwat/wat.pdb','r').readlines()
list_wat3 = []
a = True
for eachline in lines:
	if a and ("ATOM  1e310" not in eachline):
		continue
	elif 'ATOM  2583d' in eachline:
		break
	else:
		a = False
		list_wat3.append(eachline)
list_wat3.append("END\n")
ff = open("./popwat/wat3.pdb",'w')
for eachline in list_wat3:
	ff.write(eachline)
ff.close()
pdb1 = trans("./popwat/wat3.pdb")
pdb1.cont = pdb1.renumber_residues()
pdb1.cont = pdb1.renumber_atoms()
ff = open("./popwat/wat3_renum.pdb",'w')
for line in pdb1.cont:
	ff.write(line+'\n')
ff.close()

#修改格式使得残基编号可读
lines = open('./popwat/wat3_renum.pdb','r').readlines()
list_wat3_final=[]
for eachline in lines:
	line = re.sub('X.',' ',eachline)
	list_wat3_final.append(line)
ff = open("./popwat/wat3_renum_modi.pdb",'w')
for eachline in list_wat3_final:
	ff.write(eachline)
ff.close()

#wat4
lines = open('./popwat/wat.pdb','r').readlines()
list_wat4 = []
a = True
for eachline in lines:
	if a and ("ATOM  2583d" not in eachline):
		continue
	elif 'END' in eachline:
		break
	else:
		a = False
		list_wat4.append(eachline)
list_wat4.append("END\n")
ff = open("./popwat/wat4.pdb",'w')
for eachline in list_wat4:
	ff.write(eachline)
ff.close()
pdb1 = trans("./popwat/wat4.pdb")
pdb1.cont = pdb1.renumber_residues()
pdb1.cont = pdb1.renumber_atoms()
ff = open("./popwat/wat4_renum.pdb",'w')
for line in pdb1.cont:
	ff.write(line+'\n')
ff.close()

#修改格式使得残基编号可读
lines = open('./popwat/wat4_renum.pdb','r').readlines()
list_wat4_final=[]
for eachline in lines:
	line = re.sub('X.',' ',eachline)
	list_wat4_final.append(line)
ff = open("./popwat/wat4_renum_modi.pdb",'w')
for eachline in list_wat4_final:
	ff.write(eachline)
ff.close()
print ('{0}\nEnd of work of water,\nNow call charmm to generate psf, crd and pdb files...'.format(50*'-'))

#调用charmm
import os
os.system("charmm -i test.inp -o ./output/test.out")

print ('{0}\nAll work has been completed, \nplease check the correctness of the output file.\n{0}'.format(50*'-'))

