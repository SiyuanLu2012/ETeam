#coding=utf-8
# coding=utf8
'''
Created on 2014-1-14
 
@author: ETHAN
'''
from doraemon.testjob.models import TestBuildHistory
from dataaccess.testjob.dal_buildhistory import DAL_BuildHistory
 
import sys
 
class TestBuildService(object):
    '''
    business for Test build
    '''
    
    @staticmethod
    def dm_addbuildhistory(testSubmition, buildnumber, buildstatus):
        buildhistory=TestBuildService.dm_initbuildhistory(testSubmition, buildnumber, buildstatus)
        DAL_BuildHistory.addbuildhistory(buildhistory)
     
    @staticmethod
    def dm_initbuildhistory(testSubmition, buildurl,buildstatus):
        buildhistory = TestBuildHistory()
        buildhistory.TBHSubmitionID = testSubmition.id
        buildhistory.TBHProductVersion= testSubmition.TPSProductVersion
        buildhistory.TBHCodeVersion=testSubmition.TPSCodeVersion
        buildhistory.TBHCodeUrl=testSubmition.TPSCodeUrl
        buildhistory.TBHPackageAddress=testSubmition.TPSPackageAddress
        buildhistory.TBHBuilStatus=buildstatus
        buildhistory.TBHBuildUrl=buildurl
        buildhistory.TBHCodeChangeLog=testSubmition.TPSCodeChangeLog
        return buildhistory
         
             
         
             
         
     
         
