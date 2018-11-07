#coding=utf-8
'''
Created on 2016-12-5

@author: Administrator
'''


from doraemon.ci.models import CaseTag
from url_filter.filtersets.django import ModelFilterSet

class CaseTagFilterSet(ModelFilterSet):
    class Meta(object):
        model = CaseTag
        fields = ['id']


        