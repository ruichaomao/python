#Generate input files for BDF calculation of pigment molecules in LH2
#2021.5.19 mrc
#python3 *py
import os
class Grasp():
    def __init__(self):
        pass
    def grasp(self,piglist,folder_name):
        folder = os.path.exists(folder_name)
        if not folder:
            os.mkdir(folder_name)
        for resid in piglist:
            xyz_list = []
            xyz_other_list2 = []
            for line in lines_l:
                line_l = line.split()
                if line_l[0] != 'TER': 
                    if line_l[4] == str(resid):
                        #print (line_l[4])
                        xyz_line = '{:<2}'.format(line_l[10])+'{:>10}'.format(line_l[5])+'{:>10}'.format(line_l[6])+'{:>10}'.format(line_l[7])
                        xyz_list.append(xyz_line)
                    else:
                        xyz_other_line = '{:<2}'.format(line_l[10])+'{:>10}'.format(line_l[9])+'{:>10}'.format(line_l[5])+'{:>10}'.format(line_l[6])+'{:>10}'.format(line_l[7])
                        xyz_other_list2.append(xyz_other_line)
            xyzfile = open(folder_name+str(resid)+'.xyz','w')
            for i in xyz_list:
                xyzfile.write(i+'\n')
            xyzfile.close()
            chargefile = open(folder_name+str(resid)+'.extcharge','w')
            chargefile.write("External charge, Point charge\n")
            #lines_noTER = [line for line in lines_l if "TER" not in line]
            chargefile.write(str(len(xyz_other_list2))+"\n")
            for i in xyz_other_list2:
                chargefile.write(i+'\n')
            chargefile.close()
            bdffile = open(folder_name+str(resid)+'.inp','w')
            bdffile.write("$COMPASS\nTitle\ninitial_fragment906 with backgroud point charges\nBasis\n6-31g\nGeometry\n")
            for i in xyz_list:
                bdffile.write(i+'\n')
            bdffile.write('End Geometry\nExtcharge\npoint\nSkeleton\nnosymm\n$END\n\n$XUANYUAN\nDirect\nSchwarz\n$END\n\n$SCF\nRKS\nDFT\ncam-b3lyp\ncharge\n0\nspin\n1\n$END\n\n$tddft\niexit\n5\n$end\n\n')
            bdffile.close()
    def grasp2(self,piglist,folder_name):
        folder = os.path.exists(folder_name)
        if not folder:
            os.mkdir(folder_name)
        residnum = len(piglist)
        num = 0
        while num < residnum:
            xyz_list = []
            xyz_other_list2 = []
            for line in lines_l:
                line_l = line.split()
                if line_l[0] != 'TER':
                    if num !=  residnum-1:
                        if line_l[4] == str(piglist[num]) or line_l[4] == str(piglist[num+1]):
                            #print (line_l[4])
                            xyz_line = '{:<2}'.format(line_l[10])+'{:>10}'.format(line_l[5])+'{:>10}'.format(line_l[6])+'{:>10}'.format(line_l[7])
                            xyz_list.append(xyz_line)
                        else:
                            xyz_other_line = '{:<2}'.format(line_l[10])+'{:>10}'.format(line_l[9])+'{:>10}'.format(line_l[5])+'{:>10}'.format(line_l[6])+'{:>10}'.format(line_l[7])
                            xyz_other_list2.append(xyz_other_line)
                    else:
                        if line_l[4] == str(piglist[num]) or line_l[4] == str(piglist[0]):
                            #print (line_l[4])
                            xyz_line = '{:<2}'.format(line_l[10])+'{:>10}'.format(line_l[5])+'{:>10}'.format(line_l[6])+'{:>10}'.format(line_l[7])
                            xyz_list.append(xyz_line)
                        else:
                            xyz_other_line = '{:<2}'.format(line_l[10])+'{:>10}'.format(line_l[9])+'{:>10}'.format(line_l[5])+'{:>10}'.format(line_l[6])+'{:>10}'.format(line_l[7])
                            xyz_other_list2.append(xyz_other_line)
            if num != residnum - 1:
                #print ("etewt",str(b800_l[num])+str(b800_l[num+1]))
                xyzfile = open(folder_name+str(piglist[num])+"+"+str(piglist[num+1])+'.xyz','w')
                for i in xyz_list:
                    xyzfile.write(i+'\n')
                xyzfile.close()
                chargefile = open(folder_name+str(piglist[num])+"+"+str(piglist[num+1])+'.extcharge','w')
                chargefile.write("External charge, Point charge\n")
                #lines_noTER = [line for line in lines_l if "TER" not in line]
                chargefile.write(str(len(xyz_other_list2))+"\n")
                for i in xyz_other_list2:
                    chargefile.write(i+'\n')
                chargefile.close()
                bdffile = open(folder_name+str(piglist[num])+"+"+str(piglist[num+1])+'.inp','w')
                bdffile.write("$COMPASS\nTitle\ninitial_fragment906 with backgroud point charges\nBasis\n6-31g\nGeometry\n")
                for i in xyz_list:
                    bdffile.write(i+'\n')
                bdffile.write('End Geometry\nExtcharge\npoint\nSkeleton\nnosymm\n$END\n\n$XUANYUAN\nDirect\nSchwarz\n$END\n\n$SCF\nRKS\nDFT\ncam-b3lyp\ncharge\n0\nspin\n1\n$END\n\n$tddft\niexit\n5\n$end\n\n')
                bdffile.close()
                num += 1
            else:
                xyzfile = open(folder_name+str(piglist[num])+"+"+str(piglist[0])+'.xyz','w')
                for i in xyz_list:
                    xyzfile.write(i+'\n')
                xyzfile.close()
                chargefile = open(folder_name+str(piglist[num])+"+"+str(piglist[0])+'.extcharge','w')
                chargefile.write("External charge, Point charge\n")
                #lines_noTER = [line for line in lines_l if "TER" not in line]
                chargefile.write(str(len(xyz_other_list2))+"\n")
                for i in xyz_other_list2:
                    chargefile.write(i+'\n')
                chargefile.close()
                bdffile = open(folder_name+str(piglist[num])+"+"+str(piglist[0])+'.inp','w')
                bdffile.write("$COMPASS\nTitle\ninitial_fragment906 with backgroud point charges\nBasis\n6-31g\nGeometry\n")
                for i in xyz_list:
                    bdffile.write(i+'\n')
                bdffile.write('End Geometry\nExtcharge\npoint\nSkeleton\nnosymm\n$END\n\n$XUANYUAN\nDirect\nSchwarz\n$END\n\n$SCF\nRKS\nDFT\ncam-b3lyp\ncharge\n0\nspin\n1\n$END\n\n$tddft\niexit\n5\n$end\n\n')
                bdffile.close()
                num += 1
    def grasp3(self,piglist1,piglist2,folder_name):
        folder = os.path.exists(folder_name)
        if not folder:
            os.mkdir(folder_name)
        residnum = len(piglist1)
        num = 0
        while num < residnum:
            xyz_list = []
            xyz_other_list2 = []
            for line in lines_l:
                line_l = line.split()
                if line_l[0] != 'TER':
                    if line_l[4] == str(piglist1[num]) or line_l[4] == str(piglist2[num]):
                        #print (line_l[4])
                        xyz_line = '{:<2}'.format(line_l[10])+'{:>10}'.format(line_l[5])+'{:>10}'.format(line_l[6])+'{:>10}'.format(line_l[7])
                        xyz_list.append(xyz_line)
                    else:
                        xyz_other_line = '{:<2}'.format(line_l[10])+'{:>10}'.format(line_l[9])+'{:>10}'.format(line_l[5])+'{:>10}'.format(line_l[6])+'{:>10}'.format(line_l[7])
                        xyz_other_list2.append(xyz_other_line)
            xyzfile = open(folder_name+str(piglist1[num])+"+"+str(piglist2[num])+'.xyz','w')
            for i in xyz_list:
                xyzfile.write(i+'\n')
            xyzfile.close()
            chargefile = open(folder_name+str(piglist1[num])+"+"+str(piglist2[num])+'.extcharge','w')
            chargefile.write("External charge, Point charge\n")
            #lines_noTER = [line for line in lines_l if "TER" not in line]
            chargefile.write(str(len(xyz_other_list2))+"\n")
            for i in xyz_other_list2:
                chargefile.write(i+'\n')
            chargefile.close()
            bdffile = open(folder_name+str(piglist1[num])+"+"+str(piglist2[num])+'.inp','w')
            bdffile.write("$COMPASS\nTitle\ninitial_fragment906 with backgroud point charges\nBasis\n6-31g\nGeometry\n")
            for i in xyz_list:
                bdffile.write(i+'\n')
            bdffile.write('End Geometry\nExtcharge\npoint\nSkeleton\nnosymm\n$END\n\n$XUANYUAN\nDirect\nSchwarz\n$END\n\n$SCF\nRKS\nDFT\ncam-b3lyp\ncharge\n0\nspin\n1\n$END\n\n$tddft\niexit\n5\n$end\n\n')
            bdffile.close()
            num += 1
#instance
if __name__ == '__main__':
    b800_l = [872,877,881,284,289,293,578,583,587]
    rg1_l = [878,875,285,290,287,579,584,581,873]
    b850_l = [879,880,882,283,286,288,291,292,294,577,580,582,585,586,588,871,874,876]
    b850_rg1_l = [880,283,288,292,577,582,586,871,876]
    b850_b800_l = [876,880,283,288,292,577,582,586,871]
    lines_l = open('1nkz_all_new.pdb','r').readlines()
    bdf_gene = Grasp()
    #1st type
    bdf_gene.grasp(b800_l,'./b800/')
    bdf_gene.grasp(rg1_l,'./rg1/')
    bdf_gene.grasp(b850_l,'./b850/')
    #2nd type
    bdf_gene.grasp2(b800_l,'./b800b800/')
    bdf_gene.grasp2(b850_l,'./b850b850/')
    bdf_gene.grasp2(rg1_l,'./rg1rg1/')
    #3rd type
    bdf_gene.grasp3(b800_l,rg1_l,'./rg1b800/')
    bdf_gene.grasp3(b850_rg1_l,rg1_l,'./rg1b850/')
    bdf_gene.grasp3(b800_l,b850_b800_l,'./b800b850/')
