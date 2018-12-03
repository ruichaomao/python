ff = open('rg1_all.pdb')
lines = ff.readlines()
ff.close()
new = []
for eachline in lines:
    if 'H1\'' in eachline:
        new.append(eachline +'TER\n')
    else:
        new.append(eachline)

ff = open('rg1_all_ter.pdb','w')
for line in new:
    ff.write(line)

ff.close()
