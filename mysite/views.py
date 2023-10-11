from django.shortcuts import render
from mysite.models import Post #
from django.http import HttpResponse #
from datetime import datetime
# Create your views here.
def homepage(request):
    posts=Post.objects.all()
    now=datetime.now()
    return render(request,'index.html',locals())
def showpost(requet,slug):
    post=Post.objects.get(slug=slug)
    #select*from post where slug=%slug
    return render(requet,'post.html',locals())
  
'''
def homepage(request): #收一個   
    posts=Post.objects.all() #select*from post
    post_lists=list()
    for counter,post in enumerate(posts):
        post_lists.append(f'No. {counter}-{post} <br>') #格式化字串 br:網頁上的換行
    return HttpResponse(post_lists)
'''   