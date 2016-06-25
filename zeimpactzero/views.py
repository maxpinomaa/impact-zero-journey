from django.shortcuts import render
from django.utils import timezone
from .models import Post

def videos_list(request):
    posts = Post.objects.filter(typeofpost='video')
    return render(request, 'zeimpactzero/videos.html', {'posts': posts})

def post_list(request):
    posts = Post.objects.filter(typeofpost='front')
    return render(request, 'zeimpactzero/post_list.html', {'posts': posts})
    
def route(request):
    posts = Post.objects.filter(typeofpost='video')
    return render(request, 'zeimpactzero/route.html', {'posts': posts})
    
def supporters(request):
    posts = Post.objects.filter(typeofpost='video')
    return render(request, 'zeimpactzero/supporters.html', {'posts': posts})
    
    
