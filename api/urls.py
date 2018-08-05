
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import ClassroomsList, ClassroomDetail, ClassroomCreate, ClassroomUpdateOrDelete

urlpatterns = [
    path('classrooms/', ClassroomsList.as_view(), name='classrooms'),
    path('classroom/<int:classroom_id>/', ClassroomDetail.as_view(), name='classroom-detail'),
    path('classroom/create/', ClassroomCreate.as_view(), name='classroom-create'),
    path('classroom/manage/<int:classroom_id>/', ClassroomUpdateOrDelete.as_view(), name='classroom-manage'),
]
