#!/bin/bash

# 设置为UTF-8编码
export LANG=en_US.UTF-8

# 设置脚本的标题（在终端窗口的标题栏中显示）  
echo -ne "\033]0;启动器\007"  

# 检查脚本是否从项目根目录运行
if [ ! -d "bat" ]; then
    echo "错误： 必须从项目根目录调用 set_git.sh。"
    exit 1
fi

# 进入bat目录并执行其中的set_git.sh脚本
# cd bat && ./set_git.sh
./bat/set_git.sh


# 以上脚本将设置UTF-8编码，确保从项目根目录运行，并执行子目录bat中的set_git.sh
