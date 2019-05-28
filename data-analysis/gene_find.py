import os
os.chdir("./")
#Looking for a list of data files
filelist = [fina for fina in os.listdir(os.getcwd()) if fina.startswith("gene.txt")]
print (filelist)
#GC content count
def count(a,b):
    return (a.count(b[0]) + a.count(b[1]))
#Determine whether it exists
def containAny(sequ,aset):
    for c in sequ:
        if c in aset:
            return True
        return False
#Input target sequence interval
print ("Please give the base pair range:\t\t(for example:1,500)")
input_bp = input ("Target sequence interval-->")
ini_bp = int(input_bp.split(',')[0])
end_bp = int(input_bp.split(',')[1])
#Loop through each file
for file in filelist:
    #Open data files and new files
    final_file = open("final" + file, "w+")
    ff = open(file, "r",encoding='UTF-8').readlines()
    seq = ff[0][ini_bp:end_bp];lenth = len(seq)
    #print (lenth,seq)
    #Define initial values and calculate the number of cycles
    ini_num = 0;end_num = 20
    cycletime = lenth - end_num + 1
    #print (cycletime)
    num = 1
    good_list = []
    while num <= cycletime:
        seq_select = seq[ini_num:end_num]
        #print (seq_select)
        #Calculate GC content and select a target sequence that satisfies certain conditions
        fre_GC = count(seq_select,["G","C"])/20
        #print (fre_GC)
        freGC_seqsel = seq_select+"--->"+str(fre_GC)
        if 0.5 <= fre_GC <= 0.7:
            good_list.append(freGC_seqsel)
        ini_num += 1;end_num += 1
        num += 1
    #print (len(good_list),good_list)
    good_list2 = []
    #Four bases cannot appear four times in succession
    for line in good_list:
        #if "AAAA" not in line and "GGGG" not in line and "CCCC" not in line and "TTTT" not in line:
        AGCT_list=["AAAA","GGGG","CCCC","TTTT"]
        if not containAny(AGCT_list,line) is None:
            good_list2.append(line)
            final_file.write(line + "\n")
    #print(len(good_list2), good_list2)
    final_file.close()
    print ("End of calculation for",file)
