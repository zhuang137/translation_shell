#!/bin/bash
#-*- coding:utf-8 -*-
echo -e "\033[1;32m"
cat <<EOF
                <author:liuzz4@lenovo.com>
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #   
#   xls --help                                                    
#   xls --config 检查当前配置信息是否正确,比如defaults.xml与names.xml的规
#             范检查                                               
#   xls --update 检查xls目录文件与库目录compxls文件.如果需要更新,则会更新库
#   xls --recreate 重新生成final_res资源目录，建议运行update后再运行    
#   xls --writexml 读取xls表格文件写入strings.xml文件                
#   xls --writexml yes 读取xls文件写入strings.xml文件，并生成节点<re   
#             sources></resources>                               
#	xls --writexml no 读取xls文件并写入strings.xml,没有<reources>节点
#   xls auto 该命令是上述四个命令的顺序执行，执行了xls --writexml no    
#   xls --insert 该命令可以将final_res目录下的strings.xml插入到指定的模  
#              块资源目录中                                        
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
EOF
echo -e "\033[0m"
declare -r TIP_CHOICE="请选择模式:[1]生成插入字段，该字段保存到各国的strings.xml文\
件中\n           [2]生成overlay资源文件，带有<resources></resources>节点"
declare -A operations
declare -i type_choice=1
declare -r TYPE_NO_NODE=1
declare -r TYPE_OVERLAY=2
T=`pwd -P`
operations=(['--help']='help1' ['--update']='update1' \
        ['--recreate']='recreate1' ['--writexml']='writexml'\
		['--config']='config1' ['auto']='auto' ['--insert']='insert')

function xls()
{
	warning
	${operations["$1"]} $2
}

function setmode()
{
	echo -e "$TIP_CHOICE"
	read -p "Enter number:" type_choice
	echo You have choose mode $type_choice
}

function warning()
{
	if [ ! -e main.py ];
	then
	    echo -e "\033[1;31m warning:current path is not \
in /home/whulzz/lzz_work/github/version_modify \033[0m"
	fi	
}
function auto()
{
	(
		cd $T
		echo -e "\033[1;32m"
		python main.py
		echo -e "\033[0m"
	)	
}

function insert()
{
	(
		cd $T
		echo -e "\033[1;32m"
		sh create_args.sh $1
		echo -e "\033[0m"
	)	
}

function help1()
{
	echo -e "\033[1;32m"
cat <<EOF
                <author:liuzz4@lenovo.com>
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #   
#   xls --help                                                    
#   xls --config 检查当前配置信息是否正确,比如defaults.xml与names.xml的规
#             范检查                                               
#   xls --update 检查xls目录文件与库目录compxls文件.如果需要更新,则会更新库
#   xls --recreate 重新生成final_res资源目录，建议运行update后再运行    
#   xls --writexml 读取xls表格文件写入strings.xml文件                
#   xls --writexml yes 读取xls文件写入strings.xml文件，并生成节点<re   
#             sources></resources>                               
#	xls --writexml no 读取xls文件并写入strings.xml,没有<reources>节点
#   xls auto 该命令是上述四个命令的顺序执行，执行了xls --writexml no    
#   xls --insert 该命令可以将final_res目录下的strings.xml插入到指定的模  
#              块资源目录中                                        
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
EOF
    echo -e "\033[0m"
}

function gettop()
{
	echo -e "\033[1;32m"
	echo $T
	echo -e "\033[0m"
}

function update1()
{
	(
		cd $T
		echo -e "\033[1;32m"
		python main.py --update
		echo -e "\033[0m"
	)
}

function recreate1()
{
	(
		cd $T
		echo -e "\033[1;32m"
		python main.py --recreate
		echo -e "\033[0m"
	)
}

function writexml()
{
	setmode
	(
		cd $T
		if [ $type_choice -eq $TYPE_OVERLAY ];
		then
		    echo -e "\033[1;32m"
		    python main.py --writexml yes
			echo -e "\033[0m"
		elif [ $type_choice -eq $TYPE_NO_NODE ];
		then
		    echo -e "\033[1;32m"
		    python main.py --writexml no
			echo -e "\033[0m"
		else
		    echo -e "\033[1;31m warning:模式输入错误，请输入正确的模式 \033[0m"
		fi
	)
}

function config1()
{
	(
		cd $T
		echo -e "\033[1;32m"
		python main.py --config
		echo -e "\033[0m"
	)
}