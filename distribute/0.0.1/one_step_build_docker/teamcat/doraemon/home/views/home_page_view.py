#coding=utf-8
# coding=utf-8
'''
Created on 2014-1-5

@author: ETHAN
'''

from django.http import HttpResponse
from django.shortcuts import redirect,render_to_response
from doraemon.home.pagefactory.home_unlogin_pageworker import HomeUnloginPageWorker
from doraemon.project.models import Project
from doraemon.project.viewmodels.vm_project import VM_Project
from json.encoder import JSONEncoder
from doraemon.settings import LOG_CONFIG




def home_page(request):
    try:
        if request.user.is_authenticated:
            return redirect("/project")
        else:
            page_worker=HomeUnloginPageWorker(request)
            return page_worker.get_welcome_page(request)
    except Exception as ex:
        message=str(ex)
    return HttpResponse(message)
    
    
    
    
    
    
    


    