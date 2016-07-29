#!/bin/bash
#-*- coding:utf-8 -*-
if [ x$1 != x ]
then
    echo "continue"
else
    echo "please be sure there are one valid path for argument"
    exit
fi
args0=$1
if [ ! -z ${args0%%/*} ];
then
    echo "\033[1;31m 请使用绝对路径.比如/packages/apps/Music/res \033[0m"
    exit
fi
HEAD="<resources xmlns:android=\"http://schemas.android.com/apk/res/android\">"
cd final_res
touch temp.txt
for file in `find . -name "strings.xml"`
do
    destXml=${args0}/./${file}
    if [ ! -e $destXml ]
    then
    echo -n "\033[1;31m ${destXml} doesn't exist\033[0m" >&2
    echo  "\033[1;32m auto creating ${destXml}-------\033[0m"
    mkdir -p  ${destXml%/*}
    (cd ${destXml%/*};touch strings.xml;)
    cat ${file} > temp.txt
    sed -i '$a\</resources>' temp.txt
    sed -i 's/<\/resources>//' ${destXml}
    cat temp.txt >> ${destXml}
    sed -i '1i\'"$HEAD"'' ${destXml}
    echo "insert success----${destXml}"
    continue
    elif [ -f ${destXml} ]
    then
    cat ${file} > temp.txt
    sed -i '$a\</resources>' temp.txt
    sed -i 's/<\/resources>//' ${destXml}
    cat temp.txt >> ${destXml}
    echo "insert success----${destXml}"
    #cat temp.txt
    else
    echo "${destXml}} is invalid"
    fi
done
#rm temp*.txt