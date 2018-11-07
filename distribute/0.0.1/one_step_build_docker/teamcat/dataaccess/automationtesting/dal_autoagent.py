#coding=utf-8
'''
Created on 2014-1-14

@author: ETHAN
'''
from doraemon.automationtesting.models import AutoAgent

class DAL_AutoAgent(object):
    '''
    data access class for TestTask model
    '''
    @staticmethod
    def get_all():
        ''' get all testtask
        '''
        return AutoAgent.objects.all()
    
    
    @staticmethod
    def add_autoagent(autoagent):
        ''' 
          add new test task
        '''
        autoagent.save()
    
    @staticmethod
    def get_autoagent(id):
        ''' get testingconfig by id
        '''
        return AutoAgent.objects.get(id=id)
    
    @staticmethod
    def get_autoagent_byname(name):
        result=False
        try:
            agents=AutoAgent.objects.all().filter(AName=name)
            if len(agents)>0:
                result=True
        except Exception as ex:
            print(ex)
        return result
    
    @staticmethod
    def get_autoagent_byip(ip):
        result=False
        try:
            agents=AutoAgent.objects.all().filter(AIP=ip)
            if len(agents)>0:
                result=True
        except Exception as ex:
            print(ex)
        return result