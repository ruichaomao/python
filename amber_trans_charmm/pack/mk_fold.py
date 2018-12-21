#coding=utf-8
import os
class foldjudge():
	def __init__(self,foldname=[]):
		self.foldname = foldname
		#print self.foldname
	def mkdir_fold(self):
		'''rename some residue-name'''
		for fdname in  self.foldname:
			a = os.path.exists(fdname)
			print "fold \'%s\'--->exit?---"%(fdname)+str(a)
			if not a:
				b = os.getcwd()
				os.mkdir(b+'/'+fdname)
				print "mkdir folder:\'%s\'"%(fdname)
if __name__ == '__main__':
	fold1 = foldjudge(['prot','ligand','popwat','output'])
	fold1.mkdir_fold()
