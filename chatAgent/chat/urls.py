from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('chat/', views.ChatView.as_view(), name='chat-list-create'),
    path('chatbot/', views.ChatbotView.as_view(), name='chatbot'),
]
