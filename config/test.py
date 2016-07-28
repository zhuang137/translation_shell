#!/usr/bin/python
#-*- coding:utf-8 -*-
import os

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
                yield line

if __name__=="__main__":
    ll=GenerateFileLines(path='defaults.xml')

    ss=GenerateFileLines(path='defaults.xml')

    ll=[x for x in ll]

    ss=list(y for y in ss)

    print ll

    print ss
