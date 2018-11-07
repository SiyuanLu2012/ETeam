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

connect(db=MONGODB['default']['DB'],alias=MONGODB['default']['ALIAS'], host=MONGODB['default']['HOST'], port=MONGODB['default']['PORT'])

class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)

class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=120)

class Post(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User)
    tags = ListField(StringField(max_length=30))
    comments = ListField(EmbeddedDocumentField(Comment))



class PostSerializer(DocumentSerializer):
    class Meta:
        model = Post
        depth = 2
#         fields = ('title','author','tags','comments')
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }
#         read_only_fields = ('id',)

class PostView(generics.ListAPIView):
    """
    An endpoint for users to view and update their profile information.
    """
    queryset=Post.objects
    serializer_class = PostSerializer
    permission_classes=(AllowAny,)
    filter_fields = ('username','is_active')

def add_user():
    user=User()
    user.email="user@user.com"
    user.first_name='zhang'
    user.last_name='tiande'
    user.save()
    comment1=Comment()
    comment1.content="sb"
    comment1.name="fdsdsfdsfdsfds"
#     comment1.save()
    post=Post()
    post.title="sb2"
    post.author=user
    post.tags=['1','2','1']
    post.comments=[comment1,comment1]
    post.save()

    
