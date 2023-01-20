from django.shortcuts import render
from .models import News


def news_home (request):
    news = News.objects.all()
    return render(request,'new/news.html', {'news':news})
