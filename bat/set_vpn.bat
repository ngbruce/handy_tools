chcp 65001
@echo off
title VPN设置
:start_vpn
cls
echo 测试方法：curl -vvvk https://www.google.com
echo https_proxy：  %https_proxy%
echo http_proxy：   %http_proxy%
echo ------------------------------
echo - 1 - 设置VPN
echo - 2 - 清除      
echo - 3 - 测试
echo ------------------------------
echo - 0 - 返回
echo ------------------------------
set "vpnsel=x"
set /p "vpnsel=请选择操作: "
rem socks5://127.0.0.1:10808
if %vpnsel%==1 (
    set http_proxy=http://localhost:10809
	set https_proxy=http://localhost:10809
) else if %vpnsel%==2 (
	set http_proxy=
	set https_proxy=
) else if %vpnsel%==3 (
	curl -vvvk https://www.google.com
	echo 执行完毕，按任意键退出 
	pause
rem	exit
) else if %vpnsel%==0 (
	echo 不操作，按任意键退出 
	rem	pause
	rem	exit
) else (
	cls
    echo 输入有误,请重新输入! 
	pause
    goto start_vpn
)
:end
