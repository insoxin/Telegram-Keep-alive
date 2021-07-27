# Telegram-Keep-alive
Telegram保活
一、简介
TG上的某些机器人经常会有每日签到拿积分的活动，虽说每天上号点一点也不麻烦，但时间久了就经常会忘记。本教程将分享一种比较简单的方法，基于TG API以及Python的第三方包Telethon，部署到VPS上，每天定时上TG自动签到

二、准备工作
1、已开启API的TG号（下面会讲述如何开启TG API）
2、国外VPS一台（或能魔法上网的软路由）
3、Python 3.5+

三、开启TG API
申请网址：https://my.telegram.org
1、输入手机号登录，注意验证码会发送至TG客户端而不会以短信形式发送
2、登录进去后选“API development tools”

3、根据下图提示输入申请信息

4、开通完成后，保存api_id、api_hash两个值


四、安装Python与Telethon
1、安装Python
检查VPS上Python的版本信息，查询命令：python --version 或 python3 --version。若版本号小于3.5.0，则需安装新版Python
这里以Debian/Ubuntu系统为例，编译安装Python 3.8.10，并替换python3、pip3的环境变量。请根据自己VPS的实际情况配置环境
apt-get update
apt-get install build-essential -y
apt-get install libncurses5-dev libncursesw5-dev libreadline6-dev -y
apt-get install libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev -y
apt-get install libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev -y
apt-get install ca-certificates -y
apt-get install libsqlite3-dev -y

wget https://www.python.org/ftp/python/3.8.10/Python-3.8.10.tar.xz
tar -Jxvf Python-3.8.10.tar.xz
cd Python-3.8.10
./configure
make && make install
复制代码


2、安装Telethon
pip3 install telethon
复制代码


五、自动签到脚本（Python版）
1、复制以下代码，根据需要修改6、7、14、16行，保存为tgsign.py
（代码被系统和谐，见附件）


2、先运行一次脚本，输入python3 tgsign.py回车，根据提示填写手机号与验证码。成功后Telethon会在当前文件夹下生成.session会话文件，以后就不用再输入验证码了（如无法生成会话文件，请检查Python内置库sqlite3是否已正常安装）


3、设置定时任务
输入crontab -e进入定时任务编辑器，添加：（根据实际情况调整，如python路径、脚本文件存放路径等）
0 6 * * * cd /root && /usr/local/bin/python3 tgsign.py
复制代码
