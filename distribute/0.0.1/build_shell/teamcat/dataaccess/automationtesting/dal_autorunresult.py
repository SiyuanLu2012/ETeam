#coding=utf-8
'''
Created on 2014-1-14

@author: ETHAN
'''
from doraemon.automationtesting.models import AutoRunResult
from django.db.models import Sum

class DAL_AutoRunResult(object):
    '''
    data access class for TestTask model
    '''
    @staticmethod
    def get_all():
        ''' get all runrresult
        '''
        return AutoRunResult.objects.all().filter(TRIsChild=0)
    
    
    @staticmethod
    def add_autorunresult(autorunrresult):
        ''' 
          add new runrresult
        '''
        autorunrresult.save()
    
    @staticmethod
    def get_autorunresult(id):
        ''' get runrresult by id
        '''
        return AutoRunResult.objects.get(id=id)