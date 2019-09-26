#coding=utf-8
import os
#change the dir
basic_inp = ['#----------------------------------------------------------------------\n', '#Test 078\n', '#Molecule: C2H4+H2O, distance 4 angstrom, C1\n', '#Basis set: CC-PVDZ\n', '#Test modules: compass, xuanyuan, scf, tddft, elecoup\n', '#   Test electronic excited state coupling based on TDDFT wavefunction.\n', '#   The 1st and 2nd excited singlet states coupling of a C2H4 and a H2O\n', '#   molecules are calculated via module elecoup.\n', '#Author: BSUO 20190829\n', '#----------------------------------------------------------------------\n', '$COMPASS\n', 'Title\n', 'CH2 Molecule test run, cc-pvqz\n', 'Basis\n', 'def2-sv(p)\n', 'Geometry\n', 'coordinate of fragment_1\n', 'End geometry\n', 'Group\n', 'C(1)\n', 'Skeleton\n', 'check\n', '$END\n', '\n', '$xuanyuan\n', 'Direct\n', 'Schwartz\n', 'RS\n', '0.33\n', '$end\n', '\n', '$scf\n', 'RKS\n', 'dft functional\n', 'cam-b3lyp\n', 'coulpot+cosx\n', 'cosxngrid\n', '35 -50\n', '20 -50\n', '20 -50\n', '20 -50\n', '15 -50\n', '$end\n', '\n', '$TDDFT\n', 'IMETHOD\n', '1\n', 'ISF\n', '0\n', 'ITDA\n', '0\n', 'IDIAG\n', '1\n', 'istore\n', '1\n', 'iexit\n', '3\n', 'AOKXC\n', 'MemJKOP\n', '2048\n', 'crit_e\n', '1.d-4\n', '$END\n', '\n', '%cp $BDFTASK.scforb $BDF_WORKDIR/$BDFTASK.scforb1\n', '$COMPASS\n', 'Title\n', 'CH2 Molecule test run, cc-pvqz\n', 'Basis\n', 'def2-sv(p)\n', 'Geometry\n', 'coordinate of fragment_2\n', 'End geometry\n', 'Group\n', 'C(1)\n', 'Skeleton\n', 'check\n', '$END\n', '\n', '$xuanyuan\n', 'Direct\n', 'Schwartz\n', 'RS\n', '0.33\n', '$end\n', '\n', '$scf\n', 'RKS\n', 'dft functional\n', 'cam-b3lyp\n', 'coulpot+cosx\n', 'cosxngrid\n', '35 -50\n', '20 -50\n', '20 -50\n', '20 -50\n', '15 -50\n', '$end\n', '\n', '$TDDFT\n', 'IMETHOD\n', '1\n', 'ISF\n', '0\n', 'ITDA\n', '0\n', 'IDIAG\n', '1\n', 'istore\n', '2\n', 'iexit\n', '3\n', 'AOKXC\n', 'MemJKOP\n', '2048\n', 'crit_e\n', '1.d-4\n', '$END\n', '%cp $BDFTASK.scforb $BDF_WORKDIR/$BDFTASK.scforb2\n', '\n', '$COMPASS\n', 'Title\n', 'CH2 Molecule test run, cc-pvqz\n', 'Basis\n', 'def2-sv(p)\n', 'Geometry\n', 'coordinate of fragment_1_second\n','coordinate of fragment_2_second\n', 'End geometry\n', 'Group\n', 'C(1)\n', 'Skeleton\n', 'Nfragment\n', '2\n', 'check\n', '$END\n', '\n', '$xuanyuan\n', 'Direct\n', 'Schwartz\n', '$end\n', '\n', '$elecoup\n', 'tddft\n', '2\n', '1 1\n','2 2\n', '$end\n', '\n', '&database\n', 'fragment 1  85\n', '1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20\n', '21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40\n', '41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60\n', '61  62  63  64  65  66  67  68  69  70  71  72  73  74  75  76  77  78  79  80\n', '81  82  83  84  85\n', 'fragment 2  118\n', '86  87  88  89  90  91  92  93  94  95  96  97  98  99 100 101 102 103 104 105 \n', '106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 \n', '126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145\n', '146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165\n', '166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185\n', '186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203\n', '&end\n']

rg1_name="./"+raw_input("rg1_file:")
bcl_name="../"+raw_input("bcl_file:")
#see the rg1 file first
os.chdir(rg1_name)
rg1_files = os.listdir(os.getcwd())
print (rg1_files)
#then goto b850 file
os.chdir(bcl_name)
bcl_files = os.listdir(os.getcwd())
print (bcl_files)
os.mkdir("../gene_input")
#loop in the b850file list
num = 0
for file in bcl_files:
    f_bcl = open(file,'r').readlines()
    bcl_coord = f_bcl[3:]
    f_rg1 = open("."+rg1_name+"/"+rg1_files[num],'r').readlines()
    rg1_coord = f_rg1[3:]
    new_inp_1 = [bcl_coord if 'coordinate of fragment_1\n' in i else i for i in basic_inp]
    new_inp_2 = [rg1_coord if 'coordinate of fragment_2\n' in i else i for i in new_inp_1]
    new_inp_3 = [bcl_coord if 'coordinate of fragment_1_second\n' in i else i for i in new_inp_2]
    new_inp_all = [rg1_coord if 'coordinate of fragment_2_second\n' in i else i for i in new_inp_3]
    #print (new_inp_all)
    mid_list = []
    #loop in the list
    num2 = 0
    for i in new_inp_all:
        if type(new_inp_all[num2])==list:
            for j in new_inp_all[num2]:
                mid_list.append(j)
        else:
            mid_list.append(i)
        num2+=1
    newfile = open("../gene_input/gene_input"+str("%03d" % num)+".inp",'w')
    for eachline in mid_list:
        newfile.write(eachline)      
    newfile.close()
    num += 1
