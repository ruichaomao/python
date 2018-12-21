#coding=utf-8
ALA_ab = ['H   ALA']
ALA_cm = ['HN  ALA']
ARG_ab = ['H   ARG','HB2 ARG','HB3 ARG','HG2 ARG','HG3 ARG','HD2 ARG','HD3 ARG']
ARG_cm = ['HN  ARG','HB1 ARG','HB2 ARG','HG1 ARG','HG2 ARG','HD1 ARG','HD2 ARG']
ASN_ab = ['H   ASN','HB2 ASN','HB3 ASN']
ASN_cm = ['HN  ASN','HB1 ASN','HB2 ASN']
ASP_ab = ['H   ASP','HB2 ASP','HB3 ASP']
ASP_cm = ['HN  ASP','HB1 ASP','HB2 ASP']
GLN_ab = ['H   GLN','HB2 GLN','HB3 GLN','HG2 GLN','HG3 GLN']
GLN_cm = ['HN  GLN','HB1 GLN','HB2 GLN','HG1 GLN','HG2 GLN',]
GLU_ab = ['H   GLU','HB2 GLU','HB3 GLU','HG2 GLU','HG3 GLU']
GLU_cm = ['HN  GLU','HB1 GLU','HB2 GLU','HG1 GLU','HG2 GLU']
GLY_ab = ['H   GLY','HA2 GLY','HA3 GLY']
GLY_cm = ['HN  GLY','HA1 GLY','HA2 GLY']
HSE_ab = ['H   HSE','HB2 HSE','HB3 HSE']
HSE_cm = ['HN  HSE','HB1 HSE','HB2 HSE']
ILE_ab = ['H   ILE','HG12 ILE','HG13 ILE','CD1 ILE','HD11 ILE','HD12 ILE','HD13 ILE']
ILE_cm = ['HN  ILE','HG11 ILE','HG12 ILE','CD  ILE','HD1  ILE','HD2  ILE','HD3  ILE']
LEU_ab = ['H   LEU','HB2 LEU','HB3 LEU']
LEU_cm = ['HN  LEU','HB1 LEU','HB2 LEU']
LYS_ab = ['H   LYS','HB2 LYS','HB3 LYS','HG2 LYS','HG3 LYS','HD2 LYS','HD3 LYS','HE2 LYS','HE3 LYS']
LYS_cm = ['HN  LYS','HB1 LYS','HB2 LYS','HG1 LYS','HG2 LYS','HD1 LYS','HD2 LYS','HE1 LYS','HE2 LYS']
MET_ab = ['H   MET','HB2 MET','HB3 MET','HG2 MET','HG3 MET']
MET_cm = ['HN  MET','HB1 MET','HB2 MET','HG1 MET','HG2 MET']
PHE_ab = ['H   PHE','HB2 PHE','HB3 PHE']
PHE_cm = ['HN  PHE','HB1 PHE','HB2 PHE']
PRO_ab = ['HD2 PRO','HD3 PRO','HG2 PRO','HG3 PRO','HB2 PRO','HB3 PRO']
PRO_cm = ['HD1 PRO','HD2 PRO','HG1 PRO','HG2 PRO','HB1 PRO','HB2 PRO']
SER_ab = ['H   SER','HB2 SER','HB3 SER','HG  SER']
SER_cm = ['HN  SER','HB1 SER','HB2 SER','HG1 SER']
THR_ab = ['H   THR']
THR_cm = ['HN  THR']
TRP_ab = ['H   TRP','HB2 TRP','HB3 TRP']
TRP_cm = ['HN  TRP','HB1 TRP','HB2 TRP']
TYR_ab = ['H   TYR','HB2 TYR','HB3 TYR']
TYR_cm = ['HN  TYR','HB1 TYR','HB2 TYR']
VAL_ab = ['H   VAL']
VAL_cm = ['HN  VAL']
CYS_ab = ['H   CYS','HB2 CYS','HB3 CYS','HG  CYS']
CYS_cm = ['HN  CYS','HB1 CYS','HB2 CYS','HG1 CYS']
a = ALA_ab + ARG_ab + ASN_ab + ASP_ab + GLN_ab + GLU_ab + GLY_ab + HSE_ab + ILE_ab + LEU_ab + LYS_ab + MET_ab + PHE_ab + PRO_ab + SER_ab + THR_ab + TRP_ab + TYR_ab + VAL_ab + CYS_ab
b = ALA_cm + ARG_cm + ASN_cm + ASP_cm + GLN_cm + GLU_cm + GLY_cm + HSE_cm + ILE_cm + LEU_cm + LYS_cm + MET_cm + PHE_cm + PRO_cm + SER_cm + THR_cm + TRP_cm + TYR_cm + VAL_cm + CYS_cm
class trans_rs(object):

	def __init__(self,file_name):
		self.file = file_name
		self.cont = []
		if isinstance(self.file,str):
			try:
				with open(self.file, 'r') as pdb_file:
					self.cont = [row.strip() for row in pdb_file.read().split('\n') if row.strip()]
			except	IOError as err:
				print(err)
		#print self.cont
	def trans_file(self):
		'''rename some residue-name'''
		lenth = len(a)
		new2 = []
		for row in self.cont:
			if row.startswith(('ATOM','HETATM','TER','ANISOU')):
				n = -1
				while n <= lenth-1:
					n += 1
					if n == lenth:
						new2.append(row)
						break
					elif a[n] in row:
						line = row.replace(a[n],b[n])
						new2.append(line)
						break
					else:
						continue
		return new2

if __name__ == '__main__':
	#接受命令行参数设置	
	import argparse
	parser = argparse.ArgumentParser(
		description='this is a simple program which trans amber_pdb to charmm_pdb',
		formatter_class=argparse.RawTextHelpFormatter
		)
	parser.add_argument('-i', '--input', help='Input PDB file')
	parser.add_argument('-o', '--output', help='Output PDB file')
	parser.add_argument('-v', '--version', action='version', version='v. 1.0')
	args = parser.parse_args()
	#调用函数
	pdb1 = trans_rs(args.input)
	pdb1.cont = pdb1.trans_file()
	#print pdb1.cont
	ff = open(args.output,'w')
	for line in pdb1.cont:
		ff.write(line+'\n')
	ff.close()
