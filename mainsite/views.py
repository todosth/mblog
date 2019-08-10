from django.shortcuts import render, HttpResponse, redirect
from django.template.loader import get_template
from .models import Post
import datetime
import time

# Create your views here.

def homepage(request):
    # step1
    # posts = Post.objects.all()
    # post_lists = list()
    # for count, post in enumerate(posts):
    #     post_lists.append("NO.{}:".format(str(count)) + str(post) + "<hr/>")
    #     post_lists.append("<small>"+str(post.body)+"</small><br/><br/>")

    # step2

    template = get_template('index.html')
    posts = Post.objects.all()
    # 2019-08-10 21:42:37
    now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    #print(locals())
    html = template.render(locals())

    return HttpResponse(html)


def showpost(request,slug):

    template = get_template("post.html")
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:

        return redirect("/")