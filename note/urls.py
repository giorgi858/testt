from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.SignupPageView.as_view(), name='signup'),
    path('form/', views.myform, name='myform'),
   
]
