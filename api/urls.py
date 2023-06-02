from django.urls import path,include
from .views import TaskAPI,RegisterAPI,LoginAPI

urlpatterns = [
    path('register/',RegisterAPI.as_view()),
    path('login/',LoginAPI.as_view()),
    path('persons/',TaskAPI.as_view())
]