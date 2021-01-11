from django.urls import path
from rule import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    #   path('upload/', views.upload, name='upload')
]
