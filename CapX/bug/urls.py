from django.urls import path
from . import views

app_name = 'bug'


urlpatterns = [
        path('<int:bug_id>/', views.view_bug, name='view_bug'),
        path('register_bugs/', views.register_bug, name='register_bug'),
        path('list_bugs/', views.list_bugs, name='list_bugs')
]
