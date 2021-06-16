from django.urls import path,include
from rest_framework import routers
from .views import *
from .models import *

router = routers.DefaultRouter()
router.register('discussion', DiscussionViewset,basename='discussion_Comment')


urlpatterns = [
    path('',include(router.urls)),
]