ff = open('protnoh_ter.pdb')
lines = ff.readlines()
ff.close()
new = []
n = 1
for eachline in lines:
    if 'TER' not in eachline and 'END' not in eachline:
        new.append(eachline)
    else:
                new.append("END")
                filename = 'protnoh'+str(n)+'.pdb'
                ff = open(filename,'w')
                for line in new:
                        ff.write(line)
                ff.close()
                n += 1
                new = []
