########2018/9/12#########
#######maoruichao########

from commands import getstatusoutput as get
from os import system as oss
import os
###########---------Input soft location----###############
soft_path = '/home3/maoruichao/software/mopac-centos/MOPAC2016.exe'
###########-------------file-obtain---------################
f_name = "/home3/maoruichao/mopac/test3/"+raw_input("folder name:")
os.chdir(f_name)
files = os.listdir(os.getcwd())
lis_file,file = [], []
for f in files:
    if 'mop' in f:
        file.append(f) 
        ff = f_name + "/" + f
        lis_file.append(ff)
print "Job name:%s" % (file)
print "Number of jobs:%d" % (len(lis_file))
#########-----------core_obtain--------####################
cor_len,core = 0, []
def get_core():
	'''Check the idle node,then output the quantity'''
	global cor_len , core
	aa = get('cpu-free-thread | grep -e 56')[1]
	bb = aa.split("\n")
	for l in bb:
	    core.append(l[0:3]) 
	print "Available node:%s" % (core)
	if "" in core:
             core.remove("")
	cor_len = len(core)
	print "Number of available nodes:%s" % (cor_len)	
############-------jobs_run------######################
file_index = 0
file_len = len(lis_file)
def run():
	'''Loop through the jobs on the available nodes'''
	global file_len, core, file_index
	bg,num = "&", 0
	print core
	#Execute commands cyclically
	while file_len > 0:
	 	print core[num],lis_file[file_index]
	 	m ="ssh %s %s %s %s" % (core[num],soft_path,lis_file[file_index],bg)
	 	file_index += 1
		print file_index
	 	print m
#r = get(m) # it can't run if a '&' behind it,but os can
	 	r = oss(m)
	 	print r
	 	num+=1
	 	file_len-=1
#If you have traversed all the nodes now, start over.
		if num > cor_len-1:
             		num = 0
			continue
	if file_len > 0:
             	pass
	else:
             	print"job down!"
########--------------Call functions----------#################
get_core()
if cor_len > 0:
	run()
else:
	print "No nodes available..."
