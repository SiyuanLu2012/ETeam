#coding=utf-8
#coding=utf-8
'''
Created on 2015-9-24

@author: Devuser
'''
from doraemon.home.pagefactory.pageworker import DevicePageWorker
from doraemon.home.pagefactory.home_template_path import Home_unloginPagePath


class HomeUnloginPageWorker(DevicePageWorker):
    '''
    项目页面生成器
    '''
    def __init__(self,request):
        '''
        Constructor
        '''
        DevicePageWorker.__init__(self, request)
        self.login_background="#FFF"

    def get_welcome_page(self,request):
        welcome_webpart=self.get_webpart_none_args(Home_unloginPagePath.home_welcome_path)
        pagefileds={"login_background":self.login_background,"welcome_page":welcome_webpart,"request":request}
        return self.get_page(pagefileds,Home_unloginPagePath.home_page_path, request)

    
        
        
    