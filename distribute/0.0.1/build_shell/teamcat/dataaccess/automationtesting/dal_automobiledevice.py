#coding=utf-8
'''
Created on 2014-1-14

@author: ETHAN
'''
from doraemon.automationtesting.models import AutoMobileDevice

from django.db.models import Q

class DAL_AutoMobileDevice(object):
    '''
    data access class for TestTask model
    '''
    @staticmethod
    def get_all():
        ''' get all mobiledevice
        '''
        return AutoMobileDevice.objects.all().filter(MDIsActive=1)
    
    
    @staticmethod
    def add_automobiledevice(automobiledevice):
        ''' 
          add new mobiledevice
        '''
        automobiledevice.save()
    
    @staticmethod
    def get_automobiledevice(id):
        ''' get mobiledevice by id
        '''
        return AutoMobileDevice.objects.get(id=id)
    
    @staticmethod
    def get_device_byos(deviceos):
        return AutoMobileDevice.objects.all().filter(MDIsActive=1).filter(MDeviceOS=deviceos).filter(~Q(MDeviceStatus=3))
        