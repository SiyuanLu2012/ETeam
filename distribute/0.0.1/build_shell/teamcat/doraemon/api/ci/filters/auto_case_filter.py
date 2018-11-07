#coding=utf-8
'''
Created on 2016-12-5

@author: Administrator
'''


from doraemon.ci.models import AutoCase
from url_filter.filtersets.django import ModelFilterSet

class AutoCaseFilterSet(ModelFilterSet):
    class Meta(object):
        model = AutoCase
        fields = ['ProjectID','id','CaseTag','InterfaceID','ModuleID','CaseType']
        exclude = ['CaseTag']


        