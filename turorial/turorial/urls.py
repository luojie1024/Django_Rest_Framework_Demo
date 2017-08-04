from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from snippets import api


router = routers.DefaultRouter()
router.register(r'users', api.UserViewSet)
router.register(r'blogs', api.BlogViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
]