#!/bin/bash
printf 'liu'
cat << EOF
    xls --help
    xls --config 检查当前配置信息是否正确，比如defaults.xml与names.xml的规范
            检查
    xls --update 检查xls目录文件与库目录compxls文件，如果需要更新，则会更新库
    xls --recreate 重新生成final_res资源目录，建议运行update后再运行
    xls --writexml 读取xls表格文件写入strings.xml文件
EOF
declare -A operations
T=`pwd -P`
operations=(['--help']='help1' ['--update']='update1' \
        ['--recreate']='recreate1' ['--writexml']='writexml'\
		['--config']='config1' ['auto']='auto')

function xls()
{
	warning
	${operations["$1"]}
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

function help1()
{
cat <<EOF
    xls --help
    xls --config 检查当前配置信息是否正确，比如defaults.xml与names.xml的规范
            检查
    xls --update 检查xls目录文件与库目录compxls文件，如果需要更新，则会更新库
    xls --recreate 重新生成final_res资源目录，建议运行update后再运行
    xls --writexml 读取xls表格文件写入strings.xml文件
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
	(
		cd $T
		python main.py --writexml
	)
}

function config1()
{
	(
		cd $T
		python main.py --config
	)
}