#!/usr/bin/python
#-*- coding:utf-8 -*-
comment='''因为xls文件夹下面的名字,比如ZH-rCN与国家文件夹values-zh-rCN大小写不对应，
或者 xls文件夹下面的比如ur.xls在compxls下面找不到values-ur.xls。
这个时候该模块就该处理这两种情况。
'''
import os,xlrd
from fileUtil import create_file
from config import XLS_PATH,COMP_PATH
class GenerateFileList(object):
    def __init__(self,path='.',isLower=False,suffix=''):
        self.path=path
        self.isLower=isLower
        self.suffix=suffix
    def __iter__(self):
        #return generator
        if self.isLower:
            return (os.path.splitext(xls)[0].lower()+self.suffix \
                for xls in os.listdir(self.path) if xls.endswith('.xls') and '~' not in xls)
        return (os.path.splitext(xls)[0]+self.suffix \
            for xls in os.listdir(self.path) if xls.endswith('.xls') and '~' not in xls)
def compXls(**kwargs):
    srcXls=kwargs.pop('srcXls',None)
    compXls=kwargs.pop('compXls',None)
    if kwargs:
        raise TypeError('arguments error,you must give two args like this:srcXls=[...],compXls=[...]')
    if not srcXls or not compXls:
        raise TypeError('list for srcXls or compXls may be null')
    diffXls=[x for x in srcXls if "values-"+x not in compXls]
    if diffXls:
        print "your xls named %r is not in compxls dir.we will update the dir now------" % (diffXls)
        print "compxls dir is only templates dir.these xls files are all 0KB"
        for xls in diffXls:
            path=os.path.join('./compxls','values-'+xls+'.xls')
            create_file(path=path)
def update_xls_name():
    compXls(srcXls=GenerateFileList(XLS_PATH,isLower=True),
        compXls=GenerateFileList(COMP_PATH,isLower=True))
    srcLowerXls=list(GenerateFileList(XLS_PATH,isLower=True))
    srcXls=list(GenerateFileList(XLS_PATH,isLower=False))
    compLowerXls=list(GenerateFileList(COMP_PATH,isLower=True))
    compXls=list(GenerateFileList(COMP_PATH,isLower=False))
    print srcXls
    for srcIndex,xls in enumerate(srcLowerXls):
        try:
            compIndex=compLowerXls.index('values-'+xls)
            #print xls,compIndex
            os.rename(os.path.join(XLS_PATH,srcXls[srcIndex]+'.xls'),os.path.join(XLS_PATH,compXls[compIndex]+'.xls'))
            print "rename success:%r,%r" % (xls,compXls[compIndex])
        except Exception,e:
            del srcLowerXls[:]
            del srcXls[:]
            del compLowerXls[:]
            del compXls[:]
            print 'update_xls_name error:index %r error' % xls
    print list(GenerateFileList(XLS_PATH,isLower=False))

def getSheetFromXls(xlsName='',index=0):
    if not xlsName:
        raise ValueError('getSheetFromXls:invalid xlsName!!!!')
    return xlrd.open_workbook(xlsName,encoding_override="utf-8").sheet_by_index(index)

def getValueFromSheet(country='',sheet=None,name=''):
    if not sheet or not name:
        raise ValueError('getValueFromSheet:sheet or name invalid!!')
    rows=sheet.nrows
    cols=sheet.ncols
    if rows<2 or cols<2:
        raise ValueError('%r xls is empty' % country)
    firstCols=sheet.col_values(0)
    firstCols=[xx.strip() for xx in firstCols]
    count=firstCols.count(name)
    if count==0:
        raise ValueError('%s.xls can\'t find name(%s)' % (country,name))
    elif count>1:
        raise ValueError('%s.xls find name(%s) more than one values' % (country,name))
    else:
        index=firstCols.index(name)
        return sheet.cell(index,1).value.encode('utf-8')


if __name__=="__main__":
    #print comment
    from config import XLS_PATH,COMP_PATH
    #compXls(srcXls=GenerateFileList(XLS_PATH,isLower=True),compXls=GenerateFileList(COMP_PATH,isLower=True))
    #update_xls_name()
