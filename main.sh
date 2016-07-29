#!/bin/bash
#-*- coding:utf-8 -*-
cat << EOF
    xls --help
    xls --config 检查当前配置信息是否正确，比如defaults.xml与names.xml的规范
            检查
    xls --update 检查xls目录文件与库目录compxls文件，如果需要更新，则会更新库
    xls --recreate 重新生成final_res资源目录，建议运行update后再运行
    xls --writexml 读取xls表格文件写入strings.xml文件
    xls --writexml yes 读取xls文件写入strings.xml文件，并生成节点<resources></resources>
    xls --writexml no 读取xls文件并写入strings.xml,没有<reources>节点
    xls auto 该命令是上述四个命令的顺序执行，执行了xls --writexml no
EOF

declare -r TIP_CHOICE="请选择模式:\[1\]生成插入字段，该字段保存到各国的strings.xml文
件中\n           \[2\]生成overlay资源文件，带有\<resources\>\<\/resources\>节点"
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
		python main.py
	)	
}

function insert()
{
	(
		cd $T
		sh create_args.sh $1
	)	
}

function help1()
{
cat <<EOF
    xls --help
    xls --config 检查当前配置信息是否正确，比如defaults.xml与names.xml的规范
            检查
    xls --update 检查xls目录文件与库目录compxls文件，如果需要更新，则会更新库
    xls --recreate 重新生成final_res资源目录，建议运行update后再运行
    xls --writexml 读取xls表格文件写入strings.xml文件
    xls --writexml yes 读取xls文件写入strings.xml文件，并生成节点<resources></resources>
	xls --writexml no 读取xls文件并写入strings.xml,没有<reources>节点
    xls auto 该命令是上述四个命令的顺序执行，执行了xls --writexml no
EOF
}

function gettop()
{
	echo $T
}

function update1()
{
	(
		cd $T
		python main.py --update
	)
}

function recreate1()
{
	(
		cd $T
		python main.py --recreate
	)
}

function writexml()
{
	setmode
	(
		cd $T
		if [ $type_choice -eq $TYPE_OVERLAY ];
		then
		    python main.py --writexml yes
		elif [ $type_choice -eq $TYPE_NO_NODE ];
		then
		    python main.py --writexml no
		else
		    echo -e "\033[1;31m warning:模式输入错误，请输入正确的模式 \033[0m"
		fi
	)
}

function config1()
{
	(
		cd $T
		python main.py --config
	)
}