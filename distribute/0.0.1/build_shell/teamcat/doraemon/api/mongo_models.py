#coding=utf-8
'''
Created on 2016-9-30

@author: Administrator
'''

from mongoengine import *
import datetime
from doraemon.settings import MONGODB
from rest_framework_mongoengine.serializers import DocumentSerializer,EmbeddedDocumentSerializer
from rest_framework_mongoengine import generics
from rest_framework.permissions import AllowAny
from rest_framework_mongoengine import fields
