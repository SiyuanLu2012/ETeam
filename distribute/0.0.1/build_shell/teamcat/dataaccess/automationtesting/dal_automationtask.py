#coding=utf-8
'''
Created on 2014-1-14

@author: ETHAN
'''
from doraemon.automationtesting.models import AutoTask
from doraemon.home.models import DicType
from doraemon.home.models import DicData

class DAL_AutomationTask(object):
    '''
    data access class for AutomationTask model
    '''
    @staticmethod
    def get_all():
        ''' get all automationtask
        '''
        return AutoTask.objects.all().filter(TaskIsActive=1)
    
    @staticmethod
    def add_automationtask(automationTask):
        ''' 
          add new test task
        '''
        automationTask.save()
    
    @staticmethod
    def get_automation_task(id):
        ''' get automationtask by id
        '''
        result=None
        try:
            result=AutoTask.objects.get(id=id)
        except Exception as ex:
            print(ex)
        return result
    
    @staticmethod
    def updatetask(automationTask):
        '''update task
        '''
        automationTask.save()
    
    @staticmethod
    def getallbrowsers():
        dicType=DicType.objects.get(DicTypeName='AutoTaskStatus')
        dicData=DicData.objects.filter(DicType_id=dicType.id)
        return dicData
    
    @staticmethod
    def taskname_exits(taskname):
        result=False
        try:
            task=AutoTask.objects.get(TaskName=taskname)
            result=True
        except Exception as ex:
            print(ex)
        return result
        
        
        