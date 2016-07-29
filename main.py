#!/usr/bin/python
#-*- coding:utf-8 -*-
from config import OVERLAY_PATH,XLS_PATH,XML_SUFFIX,PATH_DEFAULTXML,PATH_NAMESXML
from fileUtil import removeDir,create_dir,create_file,writeNameAndValue
from fileUtil import writeNode
from xlsUtil import GenerateFileList,update_xls_name,getSheetFromXls,getValueFromSheet
import os,itertools,sys
from config import NODE_HEADER,NODE_TAIL
from checkConfig import GenerateFileLines,XML_exist,XML_line_comp
commands=['--help','--config','--update','--recreate','--writexml','default']
operator={}
comment='''
    1)python main.py --config 检测当前配置文件defaults.xml,name.xml
    2)python main.py --update 将xls目录与compxls目录比较，并更改xls文件名
    3)python main.py --recreate 删除final_res目录并重建
    4)python main.py --writexml 读取xls文件并写入到对应国家下的strings.xml文件中
    5)python main.py 默认的命令，将上述4条顺序执行
'''
def recreate_final_dir():
	removeDir(dirName=OVERLAY_PATH)
	create_dir(path=OVERLAY_PATH)
	srcXls=GenerateFileList(path=XLS_PATH)
	for srcXx in srcXls:
		create_dir(path=os.path.join(OVERLAY_PATH,srcXx))
		create_file(path=os.path.join(OVERLAY_PATH,srcXx,'strings.xml'))
		print "create_file successly:%r" % os.path.join(OVERLAY_PATH,srcXx,'strings.xml')

def writeStringToXml(nodeNeed=False):
	if not isinstance(nodeNeed,bool):
		raise ValueError("writeStringToXml:nodeNeed must be bool(True or False)")
	srcXls=GenerateFileList(path=XLS_PATH)
	defaults=GenerateFileLines(path=PATH_DEFAULTXML)
	names=GenerateFileLines(path=PATH_NAMESXML)
	for xx in srcXls:
		values=[]
		if not xx.startswith('values-'):
			print "error:请先运行--update 选项修正xls目录名字"
			exit()
		xlsPath=os.path.join(XLS_PATH,xx+'.xls')
		strXmlPath=os.path.join(OVERLAY_PATH,xx,'strings.xml')
		sheet=getSheetFromXls(xlsName=xlsPath)
		for dd in defaults:
			values.append(getValueFromSheet(country=xx,sheet=sheet,name=dd))
		#print values,xlsPath
		if nodeNeed:
			writeNode(path=strXmlPath,nodeDes=NODE_HEADER)
		for name,value in itertools.izip(names,values):
			writeNameAndValue(path=strXmlPath,name=name,value=value)
		values=[]
		if nodeNeed:
			writeNode(path=strXmlPath,nodeDes=NODE_TAIL)

def help():
	print comment

def config():
	XML_exist()
	XML_line_comp()

def update():
	update_xls_name()

def recreate():
	recreate_final_dir()

def writexml(nodeNeed=False):
	writeStringToXml(nodeNeed)

def allExe():
	config()
	update()
	recreate()
	writexml()

operator={'--help':help,'--config':config,'--update':update,\
    '--recreate':recreate,'--writexml':writexml}
extras={'yes':True,'no':False}


if __name__=="__main__":
	args=sys.argv
	if len(args)==1:
		allExe()
	elif len(args)>3:
		raise ValueError('invalid argument,only need one argument')
	elif len(args)==3:
		try:
			operator.get(args[1])(extras.get(args[2]))
		except Exception,e:
		    print e
	else:
		try:
			operator.get(args[1])()
		except Exception,e:
		    raise ValueError('invalid argument %s'% args[1])