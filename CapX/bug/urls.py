from django.urls import path
from . import views

app_name = 'bug'

urlpatterns = [
            path('view/', views.your_view_function, name='your_view_name'),
            ]
