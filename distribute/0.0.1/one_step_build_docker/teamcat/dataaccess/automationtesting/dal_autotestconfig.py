#coding=utf-8
'''
Created on 2014-1-14

@author: ETHAN
'''
from doraemon.automationtesting.models import AutoTestConfig

class DAL_AutoTestConfig(object):
    '''
    data access class for TestTask model
    '''
    @staticmethod
    def get_all():
        ''' get all testtask
        '''
        return AutoTestConfig.objects.all()
    
    @staticmethod
    def get_all_by_projectid(projectid):
        if projectid==0:
            return DAL_AutoTestConfig.get_all().filter(TCFIsActive=1)
        else:
            return AutoTestConfig.objects.filter(TCFProjectID=projectid).filter(TCFIsActive=1)
    
    @staticmethod
    def add_autotestconfig(testingconfig):
        ''' 
          add new test task
        '''
        testingconfig.save()
    
    @staticmethod
    def get_autotest_config(id):
        ''' get testingconfig by id
        '''
        return AutoTestConfig.objects.get(id=id)
    
    @staticmethod
    def check_name_exits(autotestconfigname):
        result=False
        try:
            autotestconfig=AutoTestConfig.objects.get(TCFName=autotestconfigname)
            result=True
        except Exception as ex:
            print(ex)
        return result