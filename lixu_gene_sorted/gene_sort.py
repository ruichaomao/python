#Define: Add the value of the elements of two list
def list_add(a,b):
    c = []
    if a:
        for i in range(len(a)):
            c.append(float(a[i])+float(b[i]))
    else:
        for i in range(len(b)):
            c.append(float(b[i]))
    return c
#sorted the lines
ff = open('test.csv','r').readlines()
ff1 = ff[1:]
ff_sort = [i.strip().split(',') for i in sorted(ff1)]
#print(ff_sort)

#define the initial values
TcTe_sum = [] 
gene_id = ff_sort[0][0]
num = 0
out_list = []
#cycles - read and write: the core of this program
while num < len(ff_sort):
    if gene_id == ff_sort[num][0]:
        TcTe = ff_sort[num][1:7]
        TcTe_sum = list_add(TcTe_sum,TcTe)
        #print (gene_id,TcTe_sum)
        try:
            if out_list[-1][0] == ff_sort[num][0]:
                out_list[-1]= gene_id.split()+TcTe_sum
        except:
            out_list.append(gene_id.split()+TcTe_sum)
#        print (out_list)
    else:
        TcTe_sum = ff_sort[num][1:7]
        gene_id = ff_sort[num][0]
        out_list.append(gene_id.split()+TcTe_sum)
#        print (gene_id,TcTe_sum)
    num += 1
#print (out_list)
#write to the newfile
newfile = open('newfile.dat','w') 
newfile.write(str(ff[0]))
for i in out_list:
    ii = [str(a) for a in i]
    newfile.write(','.join(ii)+'\n')
newfile.close()
