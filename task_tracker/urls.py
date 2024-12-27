"""
URL configuration for todo_list project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.task_tracker, name='task_tracker')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='task_tracker')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from task_tracker.views import (TagListView,
                                IndexView,
                                TaskCreateView,
                                TagCreateView,
                                TagUpdateView,
                                TagDeleteView,
                                TaskUpdateView,
                                TaskDeleteView,
                                TaskCompletedView,
                                TaskUndoView)

urlpatterns = [
    path('',
         IndexView.as_view(),
         name='index'),
    path('tags/',
         TagListView.as_view(),
         name='tag-list'),
    path('task-create/',
         TaskCreateView.as_view(),
         name='task-create'),
    path('task-update/<int:pk>/',
         TaskUpdateView.as_view(),
         name='task-update'),
    path('task-delete/<int:pk>/',
         TaskDeleteView.as_view(),
         name='task-delete'),
    path('task-complete/<int:pk>/',
         TaskCompletedView.as_view(),
         name='task-complete'),
    path('task-undo/<int:pk>/',
         TaskUndoView.as_view(),
         name='task-undo'),
    path('tag-create/',
         TagCreateView.as_view(),
         name='tag-create'),
    path('tag-update/<int:pk>/',
         TagUpdateView.as_view(),
         name='tag-update'),
    path('tag-delete/<int:pk>/',
         TagDeleteView.as_view(),
         name='tag-delete'),
]


app_name = 'task_tracker'
