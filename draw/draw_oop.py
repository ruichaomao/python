#2019.8.6mrc for rmsd
import matplotlib.pyplot as plt
#import matplotlib.mlab as mlab
from scipy.stats import norm
import numpy as np
class draw():
    def __init__(self):
        pass
    '''This function is to draw rmsd diagram'''
    def drawrmsd(self,filelist=[]):
        #user-defined:color,linewidth,linestyle,marker
        self.color = ['k','r','b','y','g','c','m','w']
        self.linewidth = ['1','1','1','2','2','2','2','2']
        self.linestyle = ['-','-','-','-.',':','--','-',':']
        self.marker = ['None','None','None','.','+','*','','','v']
        self.filelist = filelist
        self.y = ["y"+str(i) for i in range(1,10)]
        self.x = ["x"+str(i) for i in range(1,10)]
        num = 0
        num2 = 0
        for filename in self.filelist:
            self.y[num] = np.loadtxt(filename)
            self.x[num] = list(range(1,len(self.y[num])+1))
            plt.plot(self.x[num],self.y[num],label=filename.split('.')[0],color=self.color[num],linewidth=self.linewidth[num],linestyle=self.linestyle[num],marker=self.marker[num])
            print (filename,self.color[num],self.linewidth[num],self.linestyle[num],self.marker[num])
            #define num2 for xlim and xticks
            if len(self.y[num]) > num2:
                num2 = len(self.y[num])      
            num += 1      
        plt.xlim((0,num2+1))
        #user-defined,change the number behind 'num2' and the range value to set up the x axis label
        plt.xticks(np.linspace(1,num2,11),[str(i)+'ns' for i in range(100,201,10)],fontsize=12)
        plt.yticks(fontsize=12)
        plt.grid(linestyle='--',linewidth=0.3)
        plt.rc('axes', axisbelow=True)
        plt.xlabel('Time(ns)',fontsize=15)
        plt.ylabel('rmsd(Ans.)',fontsize=15)
        #plt.title('RMSD show',fontsize=20)
        plt.legend()
        plt.show()
    '''This function is to draw gaussian distribution diagram'''
    def drawdistri(self,filelist=[]):
        self.facecolor=['r','b','y']
        self.linecolor=['r','b--','y-.']
        self.label=['270k','300k','330k']
        self.filelist = filelist
        num = 0
        for filename in self.filelist:
            data = []
            fp = open(filename,'r').readlines()
            for x in fp:
                aa = float(x.strip())
                data.append(aa)
            mu = np.mean(data)
            sigma = np.std(data)
            num_bins = 50
            n,bins,patches = plt.hist(data,num_bins,density=1,facecolor=self.facecolor[num],alpha=0.07)
            y1 = norm.pdf(bins,mu,sigma)
            plt.plot(bins,y1,self.linecolor[num],label=self.label[num],linewidth=3)
            num +=1
        plt.grid(linestyle='--',linewidth=0.3)
        plt.rc('axes', axisbelow=True)
        plt.xlabel('distance',fontsize=15)
        plt.ylabel('Probability Density',fontsize=15)
        plt.title('Probability Density Function',fontsize=20)
        plt.legend()
        plt.show()
    '''This function is able to draw several gaussian distribution diagrams in a canvas'''
    def draw4distri(self,filelist0=[],filelist1=[],filelist2=[],filelist3=[]):
        self.facecolor=['r','b','y']
        self.linecolor=['r','b--','y-.']
        self.label=['270k','300k','330k']
        self.filelist = [filelist0,filelist1,filelist2,filelist3]
        self.subdraw = [221,222,223,224]
        num2 = 0
        for filelist in self.filelist:
            num = 0
            plt.subplot(self.subdraw[num2])
            for filename in filelist:
                #plt.subplot(221)
                data = []
                fp = open(filename,'r').readlines()
                for x in fp:
                    aa = float(x.strip())
                    data.append(aa)
                mu = np.mean(data)
                sigma = np.std(data)
                num_bins = 50
                n,bins,patches = plt.hist(data,num_bins,density=1,facecolor=self.facecolor[num],alpha=0.07)
                y1 = norm.pdf(bins,mu,sigma)
                plt.plot(bins,y1,self.linecolor[num],label=self.label[num],linewidth=3)
                num +=1
                plt.grid(linestyle='--',linewidth=0.3)
                plt.rc('axes', axisbelow=True)
                plt.xlabel('distance',fontsize=15)
                plt.ylabel('Probability Density',fontsize=15)
                plt.legend()
                #plt.title('Data-distribution',fontsize=15)
            num2+=1
        plt.suptitle('Probability Density Function',fontsize=20)
        plt.show()
if __name__ == '__main__':
    draw_task1 = draw()
    draw_task2 = draw()
    draw_task1.drawrmsd(['270.dat','300.dat','330.dat'])
    draw_task1.drawdistri(['270.dat','300.dat','330.dat'])
    draw_task2.draw4distri(['270_s2s2.dat','300_s2s2.dat','330_s2s2.dat'],['270_s1s1.dat','300_s1s1.dat','330_s1s1.dat'],['270.dat','300.dat','330.dat'],['270_dis.dat','300_dis.dat','330_dis.dat'])
