@echo off
chcp 65001
rem 作为命令行启动的快捷入口
rem 可以使用 envirment.bat 使用本地复制的python环境
rem 如果在conda 环境中使用，应注释掉 call envirment.bat
:start_env
title 启动器 - 配置环境
cls
set "envsel=x"
echo ---------------------------------------
echo - 1 - 执行environment.bat 配置本地集成环境
echo - 2 - 不更改环境配置继续运行.
echo - 3 - 激活conda环境，手动运行(exit退出)
echo - 4 - VPN 设置
echo - 5 - 打开文件夹.
echo - 6 - Git
echo - 7 - 使用命令行
echo ---------------------------------------
set /p "envsel=请选择Python运行环境: "
if %envsel%==1 (
    call bat\environment.bat 
) else if %envsel%==2 (
	cls
    echo 环境配置未更改
) else if %envsel%==3 ( 
	cls
	title Poe/Slack 启动器 -conda环境 输入exit 退出
    %windir%\System32\cmd.exe "/K" F:\Installed_Soft\Anaconda3\Scripts\activate.bat F:\Installed_Soft\Anaconda3\envs\new3109cc
	echo 已退出conda环境
	pause
	goto start_env
rem	exit
) else if %envsel%==4 ( 
	call bat\set_vpn.bat
	goto start_env
rem	exit
) else if %envsel%==5 ( 
	explorer .\
	goto start_env
) else if %envsel%==6 (
	call bat\set_git.bat
	goto start_env
) else if %envsel%==7 (
	title 命令行 输入exit 退出
	%windir%\System32\cmd.exe
	echo 已退出命令行
	pause
	goto start_env
) else (
	cls
    echo 输入有误,请重新输入!
    goto start_env
)

setlocal enabledelayedexpansion
:start_sel
title 启动器 - 选择程序 - 待编写
set CLIENT_TYPE=unknown
set "index=1"
set "selected="
echo ------------------------------
rem 列出以 "run-" 开头的 .bat 文件 如果 for /r 参数，会搜索子目录 
for  %%F in (bat\run-*.bat) do (
    echo [!index!] %%~nxF
    set "batfile[!index!]=%%~fF"
    set /a "index+=1"
)
echo ------------------------------
echo [0] 返回
echo [d] 列出记录文件 
echo ------------------------------
set "selection=x"
set /p "selection=请输入要执行的文件序号: "
if %selection%==0 (
	goto start_env
) else if %selection%==d ( 
	cls
	echo 以下列出 records\*.json 记录文件 
	echo ------------------------------
	dir /a-d records\*.json
	rem 如果只列出文件名，加参数 /b
	goto start_sel
rem	exit
) 
	
rem 检查输入是否有效
if defined batfile[%selection%] (
    set "selected=!batfile[%selection%]!"
) else (
    cls
    echo 输入有误,请重新输入!
rem    exit /b
    goto start_sel
)

rem 执行选择的 .bat 文件
call "!selected!"
echo ------------------------------
echo 执行完毕，按任意键返回
pause
cls
goto start_sel
rem 使用exit 可以退出，即使快捷方式有参数 "K"
rem exit
rem exit /b
endlocal
:start_cmd