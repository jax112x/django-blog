from django.shortcuts import render,get_object_or_404
from .models import Post

def index(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]

    return render(request,"blog/index.html",{
        "posts" : latest_posts
    })

def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request,"blog/posts.html",{
        "posts" : all_posts
    })

def post_details(request,slug):
    current_post = get_object_or_404(Post,slug=slug)
    return render(request,"blog/post_details.html",{
        "post" : current_post,
        "tags" : current_post.tags.all()
    })

