from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'todoList'

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'), name='home-page'),
    path('register', views.register, name='register'),
    path('login', views.Login.as_view(), name='login'),
    path('logout', views.logout, name='logout')
]