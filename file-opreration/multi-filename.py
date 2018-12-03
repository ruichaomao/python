#coding=utf-8
#赋予变量初始值
a = 2
b=2
#大循环里面小变量，使打印出２８个文件
while a<=28:
        line = 1
　　　　　　　#打开两个文件
        ff = open("pro"+str(a)+".mop","w")
        f = open ("pro1.mop","r")
　　　　　　 #小循环使一行一行打印，并修改某一行的值
        while line:
                line = f.readline().strip()
                print (line)
                if "PM7" in line:
                        line = line.replace("1",str(a))
                        print (line)
                        print >> ff,line
                else:
                        print >> ff,line
　　　　　　　　#在大循环里面循环关闭２８个文件 
        ff.close()
        a+=1
        b+=1
f.close()
