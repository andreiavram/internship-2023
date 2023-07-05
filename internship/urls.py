"""
URL configuration for internship project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from todo.api.views import TaskItemList, TaskItemDetail
from todo.api.viewsets import TaskItemViewSet, DocumentViewSet
from todo.views import TaskListView, TaskDetailView

router = DefaultRouter()
router.register("tasks", TaskItemViewSet, basename="task")
router.register("documents", DocumentViewSet, basename="document")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('tasks/', TaskListView.as_view(), name="task_list"),
    path('tasks/<int:pk>/<str:bla>/', TaskDetailView.as_view(), name="task_detail"),

    # path('api/tasks/', TaskItemList.as_view(), name="api_task_list"),
    # path('api/tasks/<int:pk>/', TaskItemDetail.as_view(), name="api_task_detail"),
    path('api/', include(router.urls)),
]
