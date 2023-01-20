from django.urls import path,include
from .views import news_home

urlpatterns = [
    path('news/', news_home, name='news' ),
]