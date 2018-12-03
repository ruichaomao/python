#coding=utf-8
import os
#改变路径
f_name="./"+raw_input("file:")
os.chdir(f_name)
#得到该目录下文件名，结果是个列表
files = os.listdir(os.getcwd())
print (files)
#设置变量
#num=0
#用for循环遍历文件名列表中的所有文件
for file in files:
	#print (file)
#对文件执行抽取操作，并在该路径下生成相应的目标文件
	f = open (file,"r")
	lines = f.readlines()
	f.close()
	#print (lines)
	#num += 1 
	position = file.rfind(".")
	newname = file[:position]+".mop"
	ff = open (newname,"w")
	#在文件头端添加关键词
	ff.seek(0,0)
	ff.write("1SCF NOGPU threads=18 vectors CIS\ndescription\ndescription2\n")
	for line in lines:
		#print (line)
		if "ATOM" in line:
			line=line.strip()
			#print(line)
			#print (line[77])
			print >> ff,(" "+line[76:78]+(" ")*10+line[31:55])
		else:
			continue
ff.close()
