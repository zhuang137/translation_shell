#!/bin/bash
#-*- coding:utf-8 -*-
if [ -e tar -a -d tar ];
then
    rm -rf tar
fi
mkdir tar
python -m py_compile *.py
cp -rf compxls tar
cp -rf config tar
cp -rf xls tar
while read line;
do
    mv $line tar
done< <(ls *.pyc|cut -f1)
(
    cd tar
    tar -zcvf transtionXLS.tar.gz *
)
