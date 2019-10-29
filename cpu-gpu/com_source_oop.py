#! coding=utf-8
#maoruichao 2019.10.24  python3
#cpu proc/all usage whouse?
import os 
import math
class Com_resource():
    def __init__(self):
        #file = os.popen("ssh n1 'getent passwd | cut -d: -f1'").readlines()
        #self.user_list=[a.strip() for a in file]
        self.user_list = ['root', 'bin', 'daemon', 'adm', 'lp', 'sync', 'shutdown', 'halt', 'mail', 'uucp', 'operator', 'games', 'gopher', 'ftp', 'nobody', 'dbus', 'usbmuxd', 'rpc', 'vcsa', 'rtkit', 'abrt', 'avahi-autoipd', 'saslauth', 'postfix', 'rpcuser', 'nfsnobody', 'haldaemon', 'gdm', 'ntp', 'apache', 'pulse', 'sshd', 'tcpdump', 'jgao', 'bdf', 'gj', 'xiem', 'bsuo', 'genli', 'jgao', 'yangjiajun', 'guojianping', 'wise', 'liuyang', 'zhangxuan', 'randy', 'horaira', 'dongtiange', 'penghui', 'demo', 'huangxh', 'liqing', 'maoruichao', 'bielihua', 'lvmengting', 'liugroup', 'hexf', 'zhaohui', 'chexin', 'sunyoumin', 'feijunwen', 'wangtao', 'git', 'xumaofeng', 'fangyaping', 'zhanghan', 'cbc', 'dingshuang']
    def proc_thread_user(self,nodelist=[]):
        proc_num_list = []
        thread_use_list = []
        user_nodelist = []
        for n in nodelist:
            os.environ['n']=str(n)
            file = os.popen("timeout 12 ssh n$n 'top -d 0 -n 2 -b | grep -i 'day' -A 100 | grep -v -e '--' | tail -n 101;cat /proc/cpuinfo | grep 'processor' | wc -l'").readlines()
            if file:
                #thread mistake sometimes,so give this Error handling...
                try:
                    int(file[-1])
                except:
                    num_proc = int(os.popen("timeout 12 ssh n$n cat /proc/cpuinfo | grep 'processor' | wc -l").readlines()[-1])
                else:
                    num_proc = int(file[-1])
                #print ("last num:"+file[-1])
                datalist = [] #toplist
                for f in file:
                    datalist.append(f.strip().split())
                #proc & user
                line_num = 7
                proc_num = 0
                user_1nodelist = []
                for i in range(0,80):
                    aa = datalist[line_num][8]
                    #print (aa)
                    bb = datalist[line_num][11]
                    #print (bb)
                    cc = datalist[line_num][1]
                    if float(aa) > 50 and bb != 'top':
                       #print (n,aa,bb,cc)
                        proc_num += 1
                        user_1nodelist.append(cc)
                    line_num += 1
                ###revise the user name
                user_num = 0
                for i in user_1nodelist:
                    for j in self.user_list:
                        if i in j:
                            user_1nodelist[user_num] = j
                    user_num += 1
                ###
                proc_num_list.append(proc_num)
                user_nodelist.append(user_1nodelist)
                #thread
                Cpu_line = datalist[2] 
                cpu_usage1 = Cpu_line[1]
                find_position = cpu_usage1.find('%')
                cpu_usage = float(cpu_usage1[:find_position])
                remain = int(math.ceil(num_proc*(cpu_usage/100)))
                #print ("Thread usage:"+str(remain)+'/'+str(num_proc))
                thread_use_list.append(str(remain)+'/'+str(num_proc))
            else:
                proc_num_list.append("Process blocking...")
                thread_use_list.append('')
                user_nodelist.append('')
        return proc_num_list,thread_use_list,user_nodelist
    def proc_thread(self,nodelist=[]):
        proc_num_list = []
        thread_use_list = []
        for n in nodelist:
            os.environ['n']=str(n)
            file = os.popen("timeout 12 ssh n$n 'top -d 0 -n 2 -b | grep -i 'day' -A 100 | grep -v -e '--' | tail -n 101;cat /proc/cpuinfo | grep 'processor' | wc -l'").readlines()
            if file:
                try:
                    int(file[-1])
                except:
                    num_proc = int(os.popen("timeout 12 ssh n$n cat /proc/cpuinfo | grep 'processor' | wc -l").readlines()[-1])
                else:
                    num_proc = int(file[-1])
                #print ("last num:"+file[-1])
                datalist = [] #toplist
                for f in file:
                    datalist.append(f.strip().split())
                #proc
                line_num = 7
                proc_num = 0
                for i in range(0,80):
                    aa = datalist[line_num][8]
                    #print (aa)
                    bb = datalist[line_num][11]
                    #print (bb)
                    if float(aa) > 50 and bb != 'top':
                        proc_num += 1
                    line_num += 1
                proc_num_list.append(proc_num)
                #thread
                Cpu_line = datalist[2] 
                cpu_usage1 = Cpu_line[1]
                find_position = cpu_usage1.find('%')
                cpu_usage = float(cpu_usage1[:find_position])
                remain = int(math.ceil(num_proc*(cpu_usage/100)))
                #print ("Thread usage:"+str(remain)+'/'+str(num_proc))
                thread_use_list.append(str(remain)+'/'+str(num_proc))
            else:
                proc_num_list.append("Process blocking...")
                thread_use_list.append('')
        return proc_num_list,thread_use_list
    def proc(self,nodelist=[]):
        #Number of processes
        proc_num_list = []
        for n in nodelist:
            os.environ['n']=str(n)
            file = os.popen("timeout 12 ssh n$n top -d 0 -n 2 -b | grep -i 'day' -A 100 | grep -v -e '--' | tail -n 101").readlines()
            if file:
                datalist = [] #toplist
                for f in file:
                    datalist.append(f.strip().split())
                line_num = 7
                proc_num = 0
                for i in range(0,80):
                    aa = datalist[line_num][8]
                    #print (aa)
                    bb = datalist[line_num][11]
                    #print (bb)
                    if float(aa) > 50 and bb != 'top':
                        proc_num += 1
                    line_num += 1
                #print ('number of proc:'+ str(proc_num))
                proc_num_list.append(proc_num)
            else:
               proc_num_list.append("process blocking...") 
        return proc_num_list
    def thread(self,nodelist=[]):
        #thread usage
        thread_use_list = []
        for n in nodelist:
            os.environ['n']=str(n)
            #num_proc = int(os.popen('ssh n$n cat /proc/cpuinfo | grep "processor" | wc -l ').read()) #proc
            #file = os.popen("ssh n$n top -d 0 -n 2 -b | grep -i 'day' -A 100 | grep -v -e '--' | tail -n 101").readlines()
            file = os.popen("timeout 12 ssh n$n 'top -d 0 -n 2 -b | grep -i 'day' -A 100 | grep -v -e '--' | tail -n 101;cat /proc/cpuinfo | grep 'processor' | wc -l'").readlines()
            if file:
                try:
                    int(file[-1])
                except:
                    num_proc = int(os.popen("timeout 12 ssh n$n cat /proc/cpuinfo | grep 'processor' | wc -l").readlines()[-1])
                else:
                    num_proc = int(file[-1])
                datalist = [] #toplist
                for f in file:
                    datalist.append(f.strip().split())
                Cpu_line = datalist[2] 
                cpu_usage1 = Cpu_line[1]
                find_position = cpu_usage1.find('%')
                cpu_usage = float(cpu_usage1[:find_position])
                remain = int(math.ceil(num_proc*(cpu_usage/100)))
                #print ("Thread usage:"+str(remain)+'/'+str(num_proc))
                thread_use_list.append(str(remain)+'/'+str(num_proc))
            else:
                thread_use_list.append("process blocking...")
        return thread_use_list

if __name__ == '__main__':
    test = Com_resource()
    #cpu_nlist = [1,2,3,4,5,6,8,10,11,14,15,16,17,18,23,24,25,26,27,28,29,31,32,33,34,35,36,37,38,39,40]
    #gpu_nlist = [7,9,12,13,19,22,41,42,43,44,45,46,47,48]
    cpu_nlist = [1,2,3,16]
    gpu_nlist = [7,12,45,46]
    haha = test.proc_thread_user(cpu_nlist)
    cpu_proc = haha[0]
    cpu_thread = haha[1]
    cpu_proc_user = haha[2]
    gaga = test.proc_thread_user(gpu_nlist)
    gpu_proc = gaga[0]
    gpu_thread = gaga[1]
    gpu_proc_user = gaga[2]
    ff = open('iinter.dat','w')
    #ff.write('     CPU-USAGE\n'+'node'+'  '+'process'+'  '+'thread\n')
    ff.write('         CPU-USAGE\n'+'node'+'  '+'process'+'  '+'thread'+'  '+'users'+'\n')
    num = 0
    for i in cpu_nlist:
        #ff.write(('{:<9}'.format('n'+(str(i))))+('{:<6}'.format(str(cpu_proc[num])))+('{:>6}'.format(str(cpu_thread[num])))+"\n")
        ff.write(('{:<9}'.format('n'+(str(i))))+('{:<6}'.format(str(cpu_proc[num])))+('{:>6}'.format(str(cpu_thread[num])))+"  "+('{:<6}'.format(','.join(list(set(cpu_proc_user[num])))))+"\n")
        num += 1
    #ff.write('     GPU-USAGE\n'+'node'+'  '+'process'+'  '+'thread\n')
    ff.write('          GPU-USAGE\n'+'node'+'  '+'process'+'  '+'thread'+'  '+'users'+'\n')
    num2 = 0
    for i in gpu_nlist:
       #ff.write(('{:<9}'.format('n'+(str(i))))+('{:<6}'.format(str(gpu_proc[num2])))+('{:>6}'.format(str(gpu_thread[num2])))+"\n")
        ff.write(('{:<9}'.format('n'+(str(i))))+('{:<6}'.format(str(gpu_proc[num2])))+('{:>6}'.format(str(gpu_thread[num2])))+"  "+('{:<6}'.format(','.join(list(set(gpu_proc_user[num2])))))+"\n")
        num2 +=1
    ff.close()
#cpu temp ---need install lm-sensors
#gpu temp
#neicun
#yonghu list
