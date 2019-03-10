import os
os.chdir("./pic_data_copy")
pw = os.getcwd()
files = os.listdir(os.getcwd())
'''def renamef(m,n,f):
	while true:
		mm = 1
	if m<= num <=n:
		ss = f*mm
		#print (pw+"/"+p_name,pw+"/"+ss+"/"+p_name)
		os.rename(pw+"/"+p_name,pw+"/"+ss+p_name)	
	mm+=1
for p_name in files:
	num =  int(p_name[:p_name.rfind(".")])
	renamef(0,100,"a")
	renamef(101,200,"b")
	renamef(201,300,"c")
	renamef(301,400,"d")
	renamef(401,500,"e")
	renamef(501,600,"f")
	renamef(601,700,"g")
	renamef(701,800,"h")
	renamef(801,900,"i")
	renamef(901,1000,"j")'''


for p_name in files:
	num =  int(p_name[:p_name.rfind(".")])
	if 0<= num <=100:
		ss = "a"*num
		print (pw+"/"+p_name,pw+"/"+ss+p_name)
		print type(ss+p_name)
		os.rename(pw+"/"+p_name,pw+"/"+ss+p_name)
	if 101<= num <=200:
		ss = "b"*(num-100)
		print (pw+"/"+p_name,pw+"/"+ss+p_name)
		print type(ss+p_name)
		os.rename(pw+"/"+p_name,pw+"/"+ss+p_name)
	if 201<= num <=300:
		ss = "c"*(num-200)
		print (pw+"/"+p_name,pw+"/"+ss+p_name)
		print type(ss+p_name)
		os.rename(pw+"/"+p_name,pw+"/"+ss+p_name)
	if 301<= num <=400:
		ss = "d"*(num-300)
		print (pw+"/"+p_name,pw+"/"+ss+p_name)
		print type(ss+p_name)
		os.rename(pw+"/"+p_name,pw+"/"+ss+p_name)
	if 401<= num <=500:
		ss = "e"*(num-400)
		print (pw+"/"+p_name,pw+"/"+ss+p_name)
		print type(ss+p_name)
		os.rename(pw+"/"+p_name,pw+"/"+ss+p_name)
	if 501<= num <=600:
		ss = "f"*(num-500)
		print (pw+"/"+p_name,pw+"/"+ss+p_name)
		print type(ss+p_name)
		os.rename(pw+"/"+p_name,pw+"/"+ss+p_name)
	if 601<= num <=700:
		ss = "g"*(num-600)
		print (pw+"/"+p_name,pw+"/"+ss+p_name)
		print type(ss+p_name)
		os.rename(pw+"/"+p_name,pw+"/"+ss+p_name)
	if 701<= num <=800:
		ss = "h"*(num-700)
		print (pw+"/"+p_name,pw+"/"+ss+p_name)
		print type(ss+p_name)
		os.rename(pw+"/"+p_name,pw+"/"+ss+p_name)
	if 801<= num <=900:
		ss = "i"*(num-800)
		print (pw+"/"+p_name,pw+"/"+ss+p_name)
		print type(ss+p_name)
		os.rename(pw+"/"+p_name,pw+"/"+ss+p_name)
	if 901<= num <=1000:
		ss = "j"*(num-900)
		print (pw+"/"+p_name,pw+"/"+ss+p_name)
		print type(ss+p_name)
		os.rename(pw+"/"+p_name,pw+"/"+ss+p_name)
