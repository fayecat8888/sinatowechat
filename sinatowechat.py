#!/usr/bin/env python
# coding: utf-8

from wxbot import *

#call sina api
import requests
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import threading

from Queue import Queue
from optparse import OptionParser

#get stock price from sinaapi



class MyWXBot(WXBot):
	def handle_msg_all(self, msg):
		#if msg['msg_type_id'] == 4 and msg['content']['type'] == 0:       
		if msg['msg_type_id'] == 3 and msg['content']['type'] == 0:
			#slice_num = 21
			#value_num = 3
			#US，SZSH，HK分片不相同，以下手动指定
			code = msg['content']['desc']
			if code[0].isalpha():
				r = requests.get("http://hq.sinajs.cn/list=%s" % (code))
				res = r.text.split(',')
				#如果是港股
				if code[0:2]=="hk" and len(res) > 1:
					name, now = r.text.split(',')[0].split('=')[1][1:], r.text.split(',')[6]
					today, yesterday, size = r.text.split(',')[2], r.text.split(',')[3], r.text.split(',')[12]
					#reply = name + "\n" + code + "\n" +"当前价:" + now + "\n"+"开盘价:" + today +"\n" +"昨日收盘价:" + yesterday +"\n"+"交易量:" + size
					
					reply = u'名称:%s\n代号:%s\n当前价:%s\n开盘价:%s\n昨收盘价:%s\n交易量(百):%s'%(name,code,now,today,yesterday,size)
					#return reply
					self.send_msg_by_uid(reply, msg['user']['id'])

				if code[0:2] == ("sz" or code[0:2] == "sh") and len(res) > 1:
					name, now = r.text.split(',')[0][21:], r.text.split(',')[1]
					today, yesterday, size = r.text.split(',')[5], r.text.split(',')[2], r.text.split(',')[10]
					#reply = name + "\n" + code + "\n" +"当前价:" + now + "\n"+"开盘价:" + today +"\n" +"昨日收盘价:" + yesterday +"\n"+"交易量:" + size
					
					reply = u'名称:%s\n代号:%s\n当前价:%s\n开盘价:%s\n昨收盘价:%s\n交易量(百):%s'%(name,code,now,today,yesterday,size)
					#return reply
					self.send_msg_by_uid(reply, msg['user']['id'])

				#如果sz sh未查到，则尝试us
				if len(res) ==1:
					r = requests.get("http://hq.sinajs.cn/list=gb_%s" % (code))
					res = r.text.split(',')
					if len(res) > 1:
						name, now = r.text.split(',')[0].split('=')[1][1:], r.text.split(',')[1]
						today, yesterday, size = r.text.split(',')[6], r.text.split(',')[26], r.text.split(',')[10]
						#reply = name + "\n" + code + "\n" +"当前价:" + now + "\n"+"开盘价:" + "\n"+"昨日收盘价:" + yesterday +"\n"+"交易量:" + size
						reply = u'名称:%s\n代号:%s\n当前价:%s\n开盘价:%s\n昨收盘价:%s\n交易量(百):%s'%(name,code,now,today,yesterday,size)
						#return reply
						self.send_msg_by_uid(reply, msg['user']['id'])
			#post到wechat的格式
			#self.send_msg_by_uid(u'hihi', msg['user']['id'])
			#self.send_img_msg_by_uid("img/1.png", msg['user']['id'])
			#self.send_file_msg_by_uid("img/1.png", msg['user']['id'])
'''
	def schedule(self):
		self.send_msg(u'张三', u'测试')
		time.sleep(1)
'''


def main():
	bot = MyWXBot()
	bot.DEBUG = True
	bot.conf['qr'] = 'png'
	bot.run()


if __name__ == '__main__':
	main()
