#!/usr/bin/env python
# coding: utf-8
#

from wxbot import *


class MyWXBot(WXBot):
    def handle_msg_all(self, msg):
        #if msg['msg_type_id'] == 4 and msg['content']['type'] == 0:
        if msg['msg_type_id'] == 3 and msg['content']['type'] == 0 and msg['content']['desc'] == "hello":
            #self.send_msg_by_uid(u'hihi', msg['user']['id'])
            self.send_msg_by_uid(u'hihi', msg['user']['id'])
            self.send_msg(u'孟迪', u'测试')
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
