# -*- coding: utf-8 -*-
import os
import time
from telethon import TelegramClient, events, sync

api_id = []	#输入api_id，一个账号一项
api_hash = ['']	#输入api_hash，一个账号一项

session_name = api_id[:]
for num in range(len(api_id)):
	session_name[num] = "id_" + str(session_name[num])
	client = TelegramClient(session_name[num], api_id[num], api_hash[num])
	client.start()
	client.send_message("@luxiaoxun_bot", '/checkin')	#第一项是机器人ID，第二项是发送的文字
	client.send_message("@hiofficialbot", '👋 领取今天奖励')
	client.send_message("@FreeSGKbot", '/sign')	#第一项是机器人ID，第二项是发送的文字
	time.sleep(10)	#延时5秒，等待机器人回应（一般是秒回应，但也有发生阻塞的可能）
	message = client.get_messages("@hiofficialbot", limit=1) #使用get_message()方法获取按钮内容
	message[0].click(password="password") #使用click()模拟点击。但click()需要两步验证密码，写到password参数后.两步验证密码在TG APP设置里开启
	time.sleep(10) #延时5秒
	client.send_message("@hiofficialbot", '1')
	client.send_read_acknowledge("@luxiaoxun_bot")	#将机器人回应设为已读
	client.send_read_acknowledge("@hiofficialbot")	#将机器人回应设为已读
	client.send_read_acknowledge("@FreeSGKbot")	#将机器人回应设为已读
	print("Done! Session name:", session_name[num])
	
os._exit(0)
