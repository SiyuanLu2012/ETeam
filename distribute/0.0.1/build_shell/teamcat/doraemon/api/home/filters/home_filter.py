#coding=utf-8
'''
Created on 2016-12-5

@author: Administrator
'''


from doraemon.project import models
from url_filter.filtersets.django import ModelFilterSet

class ProjectTaskFilterSet(ModelFilterSet):
    class Meta(object):
        model = models.Task
        fields = ['ProjectID','Status']


