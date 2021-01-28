#2021.1.26
#MaoRuichao
#Command: python absorption.py ./log_folder
#Drive the script with python3 to generate the absorption data
#PS: For the diffrence bettween BDF and Gaussian output files, users can modify the definitions of functions in dipole_get, excited_get, atom_coord_get by themselves. 
import os
import sys 
import math
import numpy as np
class Absorption():
    def __init__(self):
        pass
    #get the electric dipole moments
    def dipole_get(self,f_list):
        if 'Gaussian System' in f_list[0]:
            keyword = [i for i in f_list if "transition electric dipole moments" in i]
            keyword_id = f_list.index(keyword[0])
            keyword_id += 2
            dipole1 = f_list[keyword_id].split()
            dipole2 = dipole1[1:4]
            dipole3 = [float(i) for i in dipole2]
            #print (dipole3)
        else:
            keyword = [i for i in f_list if "electric dipole moments" in i]
            keyword_id = f_list.index(keyword[0])
            keyword_id += 2
            dipole1 = f_list[keyword_id].split()
            dipole2 = dipole1[1:4]
            dipole3 = [float(i) for i in dipole2]
            #print (dipole3)
        return dipole3
 
    #get the the adjusted dipole
    def adjust_dipole_get(self,f_list):
        dipole3 = self.dipole_get(f_list)
        dipole4 = np.array(dipole3)
        NB_coord = self.atom_coord_get(f_list)[1]
        ND_coord = self.atom_coord_get(f_list)[2]
        NB_ND = np.array([(ND_coord[i]-NB_coord[i]) for i in range(3)]) #Pay attention to the direction
        #print ("flag1",dipole4,NB_ND)
        if np.dot(dipole4,NB_ND) < 0:
            #print (np.dot(dipole4,NB_ND))
            adjust_dipole = [-i for i in dipole4]
        else:
            adjust_dipole = dipole4
        #print (adjust_dipole)
        return adjust_dipole

    #get the excited values
    def excited_get(self,f_list):
        if 'Gaussian System' in f_list[0]:
            keyword = [i for i in f_list if "Excited State   1" in i]
            keyword_id = f_list.index(keyword[0])
            excited1 = f_list[keyword_id].split()
            excited2 = excited1[4]
            excited3 = float(excited2)
            #print (excited3)
        else:
            keyword = [i for i in f_list if "1   A    2   A" in i]
            keyword_id = f_list.index(keyword[0])
            excited1 = f_list[keyword_id].split()
            excited2 = excited1[4]
            excited3 = float(excited2)
        #print (excited3)
        return excited3
    #get the atomic coordinates of MG,NB,ND
    def atom_coord_get(self,f_list):
        if 'Gaussian System' in f_list[0]:
            keyword = [i for i in f_list if "Multiplicity" in i]
            keyword_id = f_list.index(keyword[0])
            MG_id = keyword_id + 1
            MG_coord1 = f_list[MG_id].split()[1:4]
            MG_coord2 = [float(i) for i in MG_coord1]         
            NB_id = keyword_id + 17
            NB_coord1 = f_list[NB_id].split()[1:4]
            NB_coord2 = [float(i) for i in NB_coord1]         
            ND_id = keyword_id + 32
            ND_coord1 = f_list[ND_id].split()[1:4]
            ND_coord2 = [float(i) for i in ND_coord1]         
            #print (MG_coord2,NB_coord2,ND_coord2)
        else:

            keyword = [i for i in f_list if i.startswith('geometry')]
            keyword_id = f_list.index(keyword[0])
            MG_id = keyword_id + 2
            MG_coord1 = f_list[MG_id].split()[1:4]
            MG_coord2 = [float(i) for i in MG_coord1]         
            NB_id = keyword_id + 18
            NB_coord1 = f_list[NB_id].split()[1:4]
            NB_coord2 = [float(i) for i in NB_coord1]         
            ND_id = keyword_id + 33
            ND_coord1 = f_list[ND_id].split()[1:4]
            ND_coord2 = [float(i) for i in ND_coord1]         
            #print (MG_coord2,NB_coord2,ND_coord2)
        return MG_coord2,NB_coord2,ND_coord2
    #get the vector and dis of each MG atoms pair, return are two arrays
    def MG_vec_norm(self,dimention,MG_coord_list):
        MG_vec=[];MG_norm=[]
        for i in range(dimention):
            for j in range(dimention):
                if i==j:
                    MG_vec.append([0.0,0.0,0.0])
                    MG_norm.append([0.0])
                else:
                    #print (i,j)
                    vec = [MG_coord_list[j][k]-MG_coord_list[i][k] for k in range(3)]
                    MG_vec.append(vec)
                    norm = [np.linalg.norm(np.array(vec))]
                    MG_norm.append(norm)
        return MG_vec,MG_norm
    #spectrum, need to recheck
    def spectrum(self,hami,dipole,dimention):
        D,V = np.linalg.eigh(hami) #eigenvalues and the eigenvectors
        sor = np.argsort(D)
        D_i = D[sor]
        D = D_i
        V_i = V[:,sor]
        V = V_i
        V = V.T
        newdipole = np.dot(V,dipole)
        nstep = 1000
        delt = 0.0124*2 #the number of gaussian depression
        step = float((D[dimention-1]-D[0])/nstep)
        k = 0
        strengths = [] # y
        energy = [] # x
        lamda = [] # x 
        start = float(D[0]-2000*step)
        end = float(D[dimention-1]+2000*step)
        #print ("strat,end,step",start,end,step)
        for i in np.arange(start, end , step):
            num_strength = 0.0
            for j in range(dimention):
                osc = np.linalg.norm(newdipole[j])**2
                flag = 0.0245*i*math.exp(-(D[j]-i)**2/(2*delt**2))*osc/(math.sqrt(2*3.14)*delt)/dimention
                num_strength = num_strength + flag
            strengths.append(num_strength)
            energy.append(i)
            lamda.append(1240/i)
        strengths = np.array(strengths).reshape(-1)
        energy = np.array(energy).reshape(-1)
        lamda = np.array(lamda).reshape(-1)
        return D,V,newdipole,strengths, lamda, energy
    #data writing 
    def write(self,data,filename,*single):
        if single == ():
            ff = open(sys.argv[1].split('/')[0]+'_out'+'/'+str(filename),'w')
            #print ("data",(data))
            #print ("datalen",len(data))
            for i in range(len(data)):
                for j in range(len(data[i])):
                    ff.write(str(data[i][j]))
                    ff.write(' ')
                ff.write('\n')
            ff.close()
        else:
            ff = open(sys.argv[1].split('/')[0]+'_out'+'/'+str(filename),'w')
            #print (single)
            #print (type(single))
            #print (type((single)[0]))
            data = np.array(data).reshape(len(data),single[0])
            for i in range(len(data)):
                for j in range(len(data[i])):
                    ff.write(str(data[i][j]))
                    ff.write(' ')
                ff.write('\n')
            ff.close()
    #data writing --- lamba+strength
    def write2(self,data1,data2,filename):
        aa = list(data1)
        bb = list(data2)
        spe_file = open(sys.argv[1].split('/')[0]+'_out'+'/'+str(filename),'w')
        for i in range(len(aa)):
            spe_file.write(str(aa[i])+' '+str(bb[i])+'\n')
        spe_file.close()

if __name__ == '__main__':
    folder_name=sys.argv[1]
    os.chdir(folder_name)
    log_files = os.listdir(os.getcwd())
    os.chdir("../")
    if not os.path.exists(folder_name.split('/')[0]+'_out'+'/'):
        print('mkdir: \n'+folder_name.split('/')[0]+'_out'+'/')
        os.mkdir(folder_name.split('/')[0]+'_out'+'/')
    else:
        print('exists: \n'+folder_name.split('/')[0]+'_out'+'/')

    test = Absorption()
    dipole_list1 = []
    excited_list1 = []
    MG_coord_list1 = []
    print ("\nlogfile list:")
    for file in log_files:
        if file.endswith('.log'):
            print (file)
            ff_file = open(folder_name+"/"+file,'r').readlines() 
            dipole_list1.append(test.adjust_dipole_get(ff_file))
            excited_list1.append(test.excited_get(ff_file))
            MG_coord_list1.append(test.atom_coord_get(ff_file)[0])
            #print ('MG',MG_coord_list1)
            #print ('dipole',dipole_list1)
            #print ('exci',excited_list1)

    #######<<<<<<  coupling computate & generate exciten hamitonian array >>>>>>#########
    dimention1 = len(log_files)
    ang_au = 1.0/0.529177  #convert ang units to au: value*ang_au
    au_ev = 27.2116 #convert au units to ev:value*au_ev
    MG_vec1,MG_norm1 = test.MG_vec_norm(dimention1,MG_coord_list1) 
    MG_vec2 = np.array(MG_vec1).reshape(dimention1,dimention1,3) #the vector 27*27array
    MG_norm2 = np.array(MG_norm1).reshape(dimention1,dimention1) #the norm 27*27array
    #print (MG_norm2)
    #Here... no correction for Dipole direction#
    hami_mat = [] #the coupling values use eV unit for compute the D, V, newdipole, strength,lamba, energy
    hami_mat_cm = [] #the coupling values use cm-1 unit for output
    for i in range(dimention1):
        ui = dipole_list1[i]
        for j in range(dimention1):
            uj = dipole_list1[j]
            norm1 = MG_norm2[i][j]*ang_au
            vec1 = MG_vec2[i][j]
            if i == j:
                hami_mat.append(excited_list1[i])
                hami_mat_cm.append(excited_list1[i])
            else:
                #the premeters: 2-N_dipole,1-MG_dipole,1-MG-norm
                Vij_au = (np.dot(ui,uj)/norm1**3)-3*(np.dot(ui, vec1)*np.dot(uj,vec1))/(norm1**3)/MG_norm2[i][j]**2
                Vij = Vij_au*au_ev
                Vij_cm = Vij * 8065.541154 #ev to cm-1
                hami_mat.append(Vij)
                hami_mat_cm.append(Vij_cm)

    hami_mat2 = np.array(hami_mat).reshape(dimention1,dimention1)
    hami_mat_cm2 = np.array(hami_mat_cm).reshape(dimention1,dimention1)

    #######<<<<<<  spectrum computate(lamba.dat,strength.dat)   >>>>>>#########
    D, V, newdipole, strength,lamba, energy = test.spectrum(hami_mat2, dipole_list1,dimention1)
    #print ("flag8",D,V,'newdipole',newdipole,'strength',strength,'lamb',lamba,'ene', energy)
    #print ("flag8",type(D),type(V),type(hami_mat2),'newdipole',newdipole,'strength',strength,'lamb',lamba,'ene', energy)
    #data writing
    test.write(hami_mat_cm2,'hamitonian.dat')    
    test.write(D,'D.dat',1)    
    test.write(V,'V.dat')    
    test.write(newdipole,'newdipole.dat')    
    test.write(energy,'energy.dat',1) 
    #test.write(strength,'strength.dat',1) 
    #test.write(lamba,'lamba.dat',1) 
    test.write2(lamba,strength,'lamba+strength.dat')
