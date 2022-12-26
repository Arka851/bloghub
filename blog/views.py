from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home(request):
    return render(request, "blog/home.html", {
        "posts": Post.objects.all()
    })


def about(request):
    return render(request, "blog/about.html")


def author(request, author_name):
    author = User.objects.get(username=author_name)
    if author:
        return render(request, "blog/author.html", {
            "author": author
        })
    pass
