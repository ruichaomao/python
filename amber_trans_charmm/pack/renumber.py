#coding=utf-8
class trans(object):
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
		#self.atom = [row.replace('ASN','SSS') for row in self.cont if row.startswith('ATOM')]
		#return self.atom
		out = list()
		for row in self.cont:
			if row.startswith(('ATOM','HETATM','TER','ANISOU')):
				row = row.replace('ASN','SSS')
				out.append(row)
		return out
	def renumber_atoms(self, start=1):
		out = list()
		count = start
		for row in self.cont:
			if len(row) > 5:
				if row.startswith(('ATOM', 'HETATM', 'TER', 'ANISOU')):
					num = str(count)
					while len(num) < 5:
						num = ' ' + num
					row = '%s%s%s' %(row[:6], num, row[11:])
					count += 1
			out.append(row)
		return out
	def renumber_residues(self, start=1, reset=False):
		out = list()
		count = start - 1
		cur_res = ''
		for row in self.cont:
			if len(row) > 25:
				if row.startswith(('ATOM', 'HETATM', 'TER', 'ANISOU')):
					next_res = row[22:27].strip() # account for letters in res., e.g., '1A'

					if next_res != cur_res:
						count += 1
						cur_res = next_res
					num = str(count)
					while len(num) < 3:
						num = ' ' + num
					new_row = '%s%s' %(row[:23], num)
					while len(new_row) < 29:
						new_row += ' '
					xcoord = row[30:38].strip()
					while len(xcoord) < 9:
						xcoord = ' ' + xcoord
					row = '%s%s%s' %(new_row, xcoord, row[38:])
					if row.startswith('TER') and reset:
						count = start - 1
			out.append(row)
		return out

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
	pdb1 = trans(args.input)
	pdb1.cont = pdb1.trans_file()
	#print pdb1.cont
	pdb1.cont = pdb1.renumber_atoms()
	pdb1.cont = pdb1.renumber_residues()
	ff = open(args.output,'w')
	for line in pdb1.cont:
		ff.write(line+'\n')
	ff.close()


