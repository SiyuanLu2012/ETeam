#coding=utf-8


class MessageQueue(object):
    '''
        消息队列接口，用于将消息添加到队列
    '''
    def __init__(self,channel_name,message):
        self.channel_name=channel_name
        self.message=message
