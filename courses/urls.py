from django.urls import path,include
from rest_framework import routers
from .views import *
from .models import *

router = routers.DefaultRouter()
router.register(r'course', CourseViewset,basename='Course')
router.register(r'batch',BatchViewset,basename='Batch')
router.register(r'posts',PostViewset,basename='Post')

urlpatterns = [
    path('',include(router.urls)),
]