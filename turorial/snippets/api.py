from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from . import models
from rest_framework import response


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Blog
        depth = 1
        fields = ('url', 'title', 'content',)


class BlogViewSet(viewsets.ModelViewSet):
    queryset = models.Blog.objects.all()
    serializer_class = BlogSerializer