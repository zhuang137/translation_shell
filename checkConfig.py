import os
from xlsUtil import GenerateFileList
from fileUtil import getFileLines
from config import PATH_CONFIG,PATH_DEFAULTXML,PATH_NAMESXML,XML_SUFFIX

def XML_exist():
	xmlList=GenerateFileList(path=PATH_CONFIG,suffix=XML_SUFFIX,category='.xml')
	print xmlList
	print [x for x in xmlList]
	print os.path.split(PATH_DEFAULTXML)[1]
	print os.path.split(PATH_NAMESXML)[1]
	if os.path.split(PATH_DEFAULTXML)[1] not in xmlList or os.path.split(PATH_NAMESXML)[1] not in xmlList:
		raise EnvironmentError('defaults.xml or names.xml doesn\'t exist')
	print 'OK'
	return True

def XML_line_comp():
	if getFileLines(fileName=PATH_DEFAULTXML) != getFileLines(fileName=PATH_NAMESXML):
		raise EnvironmentError('Lines doesn\'t equal between defaults.xml and names.xml')
	return True

class GenerateFileLines(object):
	def __init__(self,path='.',mode='rb'):
		self.path=path
		self.mode=mode
	def __iter__(self):
		with open(self.path,mode=self.mode) as ff:
			for line in ff.readlines():
				line=line.strip().strip('\n')
				if not line or line.startswith('#'):
					continue
				yield line.encode('utf-8')
if __name__=='__main__':
	pass