from django.urls import path
from . import views

app_name = 'bug'

urlpatterns = [
            path('view/', views.your_view_function, name='your_view_name'),
            path('register/', views.register_bug, name='register_bug'),
            path('bug/<int:bug_id>/', views.view_bug, name='view_bug'),
            ]
