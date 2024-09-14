
from django.urls import path
from . import views 
urlpatterns = [
    path('',views.AskToYaana, name='AskToYaana'),    
    path('register/', views.registerpage, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('record/<str:pk>/', views.record_detail, name='record_detail'),  # New URL pattern for detail view
]

from django.urls import path
from . import views 
urlpatterns = [
    path('',views.AskToYaana, name='AskToYaana'),    
    path('register/', views.registerpage, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('record/<str:pk>/', views.record_detail, name='record_detail'),  # New URL pattern for detail view
]
