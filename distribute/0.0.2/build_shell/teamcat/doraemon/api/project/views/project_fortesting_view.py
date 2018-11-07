# coding=utf-8
# coding=utf-8
'''
Created on 2014-1-5

@author: zhangtiande
'''
from django.http import HttpResponse
from gatesidelib.common.simplelogger import SimpleLogger
from rest_framework import generics, status, response
from doraemon.api.project.serializer import project_serializer
from rest_framework.permissions import AllowAny
from doraemon.project import models
from doraemon.home.models import FileInfo
from doraemon.settings import WEB_HOST
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from doraemon.api.project.views.CsrfExemptSessionAuthentication import CsrfExemptSessionAuthentication
from doraemon.api.project.filters import project_filter
from doraemon.api.project.filters.project_pagination import ProjectPagination
from business.project.fortesting_service import ForTestingService


class ProjectFortestingListView(generics.ListCreateAPIView):
    """
    get:
        /api/project/project_id/fortestings
        get fortesting list with project_id
        FilterSet: Null
        FilterOperation:=,__in,__gt,__contains,__icontains,Range__in,__lt,!=,__isnull

    post:
        create new fortesting
    """
    serializer_class = project_serializer.ProjectForTestingSerializer
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    pagination_class = ProjectPagination

    def get_queryset(self):
        project_id = int(self.kwargs['project_id'])
        version_id = int(self.kwargs['version_id'])
        if str(project_id) != '0':
            if str(version_id) != '0':
                qs = models.TestApplication.objects.project_fortestings(project_id).filter(
                    VersionID=int(version_id)).order_by('-id')
            else:
                qs = models.TestApplication.objects.project_fortestings(project_id).order_by('-id')
        else:
            qs = ForTestingService.get_my_fortestings(self.request)
        return project_filter.ProjectFortestingFilterSet(data=self.request.GET, queryset=qs).filter()

    def create(self, request, *args, **kwargs):
        # print(request.data)
        fortesting = ForTestingService.create_fortesting(request.data, request.user)
        serializer = project_serializer.ProjectForTestingSerializer(instance=fortesting, data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ProjectFortestingView(generics.RetrieveUpdateDestroyAPIView):
    """
    /api/project/fortesting/fortesting_id
    get,update,delete fortesting with fortesting_id
    """
    serializer_class = project_serializer.ProjectForTestingSerializer
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def get_object(self):
        fortesting_id = int(self.kwargs['fortesting_id'])
        fortesting = models.TestApplication.objects.get(fortesting_id)
        return fortesting


class ProjectFortestingUpdateStatusView(generics.UpdateAPIView):
    """
    /api/project/fortesting/fortesting_id/update_status
    update fortesting status
    """
    serializer_class = project_serializer.ProjectForTestingSerializer
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def patch(self, request, *args, **kwargs):
        fortesting_id = int(self.kwargs['fortesting_id'])
        status = request.data.get("Status", 0)
        result = [False,""]
        try:
            result = ForTestingService.update_fortesting_status(request.user, fortesting_id, status)
        except Exception as ex:
            SimpleLogger.exception(ex)
        return response.Response({'Status':result[0],'message': result[1]})


class ProjectFortestingAttachementView(generics.CreateAPIView,generics.DestroyAPIView):
    """
    /api/project/fortesting/upload_files
    upload fortesing attachment
    """
    serializer_class = project_serializer.ProjectForTestingSerializer
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    pagination_class = ProjectPagination

    def post(self, request, *args, **kwargs):
        message = ForTestingService.attachments_upload_handler(request.FILES['file'])
        return response.Response({'file_id':message[0],'url': WEB_HOST+'/project/fortesting/download/'+str(message[0])})

    def delete(self,request, *args, **kwargs):
        file_id = kwargs.get('file_id')
        ForTestingService.delete_file(file_id)
        return response.Response(status=status.HTTP_204_NO_CONTENT)
