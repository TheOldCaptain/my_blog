from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from . import models


def index_page(request):
    articles = models.Article.objects.all()
    return render(request, 'index.html', {'articles': articles})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'post.html', {'article': article})


def about_page(request):
    return render(request, 'about.html')


def contact_page(request):
    return render(request, 'contact.html')


def edit_page(request):
    return render(request, 'edit.html')


def edit_action(request, article_id):
    title = request.GET.get('title', 'TITLE')
    category = request.GET.get('category', 'CATEGORY')
    content = request.GET.get('content', 'CONTENT')
    if article_id == '0':
        article = models.Article.objects.create(title=title, category=category, content=content)
    else:
        article = models.Article.objects.get(pk=article_id)
        article.title = title
        article.category = category
        article.content = content
        article.save()
    return render(request, 'post.html', {'article': article})


def login_page(request):
    return render(request, 'login.html')


def modify_login(request, article_id):
    return render(request, 'login.html', {'article_id': article_id})


def login_action(request):
    article_id = request.POST.get('article_id')
    uname = request.POST.get('username')
    password = request.POST.get('password')
    for user in models.BlogUser.objects.all():
        if user.username == uname and user.password == password:
            if article_id == '0':
                return render(request, 'edit.html')
            else:
                article = models.Article.objects.get(pk=article_id)
                return render(request, 'edit.html', {'article': article})
    return render(request, 'login.html')


def message_page(request):
    messages = models.Message.objects.all()
    return render(request, 'message.html', {'messages': messages})


def message_onshow(request):
    nickname = request.GET.get('name', 'NAME')
    content = request.GET.get('content', 'CONTENT')
    models.Message.objects.create(nickname=nickname, content=content)
    messages = models.Message.objects.all()
    return HttpResponseRedirect('/blog/message/')
    # return render(request, 'message.html', {'messages': messages})
