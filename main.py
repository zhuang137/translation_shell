#!/usr/bin/python
from config import OVERLAY_PATH,XLS_PATH,XML_SUFFIX,PATH_DEFAULTXML,PATH_NAMESXML
from fileUtil import removeDir,create_dir,create_file,writeNameAndValue
from xlsUtil import GenerateFileList,update_xls_name,getSheetFromXls,getValueFromSheet
import os,itertools
from checkConfig import GenerateFileLines
def recreate_final_dir():
	removeDir(dirName=OVERLAY_PATH)
	create_dir(path=OVERLAY_PATH)
	srcXls=GenerateFileList(path=XLS_PATH)
	for srcXx in srcXls:
		create_dir(path=os.path.join(OVERLAY_PATH,srcXx))
		create_file(path=os.path.join(OVERLAY_PATH,srcXx,'strings.xml'))
		print "create_file successly:%r" % os.path.join(OVERLAY_PATH,srcXx,'strings.xml')

def writeStringToXml():
	srcXls=GenerateFileList(path=XLS_PATH)
	defaults=GenerateFileLines(path=PATH_DEFAULTXML)
	names=GenerateFileLines(path=PATH_NAMESXML)
	for xx in srcXls:
		values=[]
		xlsPath=os.path.join(XLS_PATH,xx+'.xls')
		strXmlPath=os.path.join(OVERLAY_PATH,xx,'strings.xml')
		sheet=getSheetFromXls(xlsName=xlsPath)
		for dd in defaults:
			values.append(getValueFromSheet(country=xx,sheet=sheet,name=dd))
		print values,xlsPath
		for name,value in itertools.izip(names,values):
			writeNameAndValue(path=strXmlPath,name=name,value=value)
		values=[]


if __name__=="__main__":
	#update_xls_name()
	#recreate_final_dir()
	recreate_final_dir()
	writeStringToXml()
	pass