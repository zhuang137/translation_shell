#!/usr/bin/python
#-*- coding:utf-8 -*-
import os
import shutil
comment='''this file provide two function.create_file(path='.') and create_dir(path='.')
'''

def create_file(**args):
    path=args.pop('path',None)
    if args:
        raise ValueError('create_file:this function only takes one argument(path="")')
    if not path:
        raise ValueError('create_file:path can\'t be None')
    try:
        with open(path,'w') as ff:
            print "create_file:%r createed successfully" % path
    except Exception,e:
        raise IOError('create_file:%r create error' % path)

def create_dir(**args):
    path=args.pop('path',None)
    if args:
        raise ValueError('create_dir:this function only takes one argument(path="")')
    if not path:
        raise ValueError('create_dir:path can\'t be None')
    os.mkdir(path)

def removeDir(dirName='.'):
    print "removing dir:%r" % dirName
    if os.path.exists(dirName) and os.path.isdir(dirName):
        shutil.rmtree(dirName)

def getFileLines(fileName=''):
    nums = 0
    try:
        with open(fileName,'rb') as ff:
            for line in ff.readlines():
                line=line.strip()
                if  not len(line) or line.startswith('#'):
                    continue
                nums += 1
    except Exception,e:
	    raise IOError('getFileLines error:fileName,%r' % fileName)     
    else:
        return nums

def writeNode(path='',nodeDes=''):
    print nodeDes+'...........'
    if not path or not nodeDes:
        raise ValueError('writeNode:path or nodeDes empty!!')
    with open(path,'a+') as ff:
        ff.write('\n')
        ff.write(nodeDes)

def writeNameAndValue(path='',name='',value=''):
    if not path or not name:
        raise ValueError('writeNode:path or name empty!!')
    with open(path,'a+') as ff:
        ff.write('\n')
        from config import STRINGS_TEMPLATE as templates
        temp=templates.replace('varName',name)
        temp=temp.replace('varValue',value)
        ff.write(temp)
        del templates

if __name__=="__main__":
    print comment
    writeNode(path='out.xml',nodeDes="rrrreeeessss")
