# chatbot/urls.py
from django.urls import path
from .views import forex_chatbot, chat_page

urlpatterns = [
    path('chat/', forex_chatbot, name='forex_chatbot'),
    path('', chat_page, name='chat_page'),
]
