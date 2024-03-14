#!/bin/bash  
  
# 设置脚本的标题（在终端窗口的标题栏中显示）  
echo -ne "\033]0;git工具\007"  
  
# 函数，用于显示菜单并获取用户选择  
display_menu() {  
    clear  
    echo "选择功能"  
    echo "------------------------------"  
    echo "- 1 - add."  
    echo "- 2 - commit -m ..."  
    echo "- 3 - push origin master"  
    echo "------------------------------"  
    echo "- 4 - fetch --all"  
    echo "- 5 - pull origin master"  
    echo "------------------------------"  
    echo "- 6 - status"  
    echo "- 7 - log"  
    echo "------------------------------"  
    echo "- 8 - set proxy"  
    echo "- 9 - unset proxy"  
    echo "------------------------------"  
    echo "- s - view global settings"  
    echo "------------------------------"  
    echo "- 0 - 退出"  
    echo "------------------------------"  
    read -p "请选择操作: " gitsel  
}  
  
# 主循环  
while true; do  
    display_menu  
      
    case $gitsel in  
        1)  
            echo "正在执行 add 命令..."  
            git add .  
            echo "add 命令执行完成，按任意键继续..."  
            read -n 1 -s  
            ;;  
        2)  
            read -p "请输入commit注释: " commit_message  
            echo "正在执行 commit 命令..."  
            git commit -m "$commit_message"  
            echo "commit 命令执行完成，按任意键继续..."  
            read -n 1 -s  
            ;;  
        3)  
            echo "正在执行 push 命令..."  
            git push origin master  
            echo "push 命令执行完成，按任意键继续..."  
            read -n 1 -s  
            ;;  
        4)  
            echo "正在执行 fetch 命令..."  
            git fetch --all  
            echo "fetch 命令执行完成，按任意键继续..."  
            read -n 1 -s  
            ;;  
        5)  
            echo "正在执行 pull 命令..."  
            git pull origin master  
            echo "pull 命令执行完成，按任意键继续..."  
            read -n 1 -s  
            ;;  
        6)  
            echo "正在执行 status 命令..."  
            git status  
            echo "status 命令执行完成，按任意键继续..."  
            read -n 1 -s  
            ;;  
        7)  
            echo "正在执行 log 命令..."  
            git log  
            echo "log 命令执行完成，按任意键继续..."  
            read -n 1 -s  
            ;;  
        8)  
            echo "正在执行设置代理..."  
            git config --global http.proxy http://127.0.0.1:20171
	    git config --global https.proxy http://127.0.0.1:20171
	    git config --global socks.proxy socks5://127.0.0.1:20170
	    echo "---------显示全局设置------------"
	    git config --global --list
	    echo ------------------------------
            echo "设置代理执行完成，按任意键继续..."  
            read -n 1 -s  
            ;;  
        9)  
            # TODO: 实现取消代理的逻辑  
            echo "正在执行取消代理..."  
            git config --global --unset http.proxy
	    git config --global --unset https.proxy
	    git config --global --unset socks.proxy
	    echo "---------显示全局设置------------"
	    git config --global --list
	    echo ------------------------------
            echo "取消代理执行完成，按任意键继续..."  
            read -n 1 -s  
            ;;  
        s)  
            echo "正在执行查看全局设置..."  
            git config --global --list
            echo "查看全局设置执行完成，按任意键继续..."  
            read -n 1 -s  
            ;;  
        0)  
            echo "退出脚本..."  
            exit 0  
            ;;  
        *)  
            echo "无效的选择，请重新输入。按任意键继续..."  
            read -n 1 -s
            ;;  
    esac  
done
