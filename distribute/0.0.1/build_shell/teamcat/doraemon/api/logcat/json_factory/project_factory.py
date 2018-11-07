#coding=utf-8
'''
Created on 2016-8-23

@author: Devuser
'''

from doraemon.api.project.viewmodel.api_project_member import ApiProjectMember
from doraemon.project.models import ProjectMember

class ProjectFactory(object):
    '''
    classdocs
    '''
    
    
    @staticmethod
    def get_member_list(request):
        result=ProjectFactory.get_project_member_instance(request)
        return result
    
    @staticmethod
    def get_project_member_instance(request):
        result=dict()
        project_id=request.GET.get("project_id")
        project_members=ProjectMember.objects.get_members(int(project_id))
        vm_member_list=list()
        for member in project_members:
            vm_project_member=ApiProjectMember(member.PMMember)
            vm_member_list.append(vm_project_member.__dict__)
        result["member_list"]=vm_member_list
        return result
                
                
        
        
        