from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_view, name='chat'),  
    path('<str:username>/', views.chat_view, name='chat'),  
]
