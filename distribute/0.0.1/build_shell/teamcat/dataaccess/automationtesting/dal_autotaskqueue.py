#coding=utf-8
'''
Created on 2015-6-10

@author: Devuser
'''

from doraemon.automationtesting.models import AutoTaskQueue

class DAL_AutoTaskQueue(object):
    
    
    
    @staticmethod
    def add_task_inqueue(queuetask):
        queuetask.save()
        
        