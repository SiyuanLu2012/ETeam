#coding=utf-8
# coding=utf-8
'''
Created on 2014-1-5

@author: ETHAN
'''
from django.http import HttpResponse
from doraemon.api.ci.json_factory.ci_factory import CIFactory
from doraemon.api.response.response_models import SuccessResponse,ErrorResponse
from business.ci.ci_agent_service import CIAgentService
from gatesidelib.common.simplelogger import SimpleLogger


def get_agent(request):
    try:
        ci_agent=CIFactory.get_agent(request)
        result=SuccessResponse("success",ci_agent)
    except Exception as ex:
        SimpleLogger.exception(ex)
        result=ErrorResponse(str(ex),dict())
        
    return HttpResponse(result.get_json())

def update_agent_status(request):
    try:
        CIAgentService.update_agent_status(request)
        result=SuccessResponse("success",dict())
    except Exception as ex:
        SimpleLogger.exception(ex)
        result=ErrorResponse(str(ex),dict())
    return HttpResponse(result.get_json())
    
    

    