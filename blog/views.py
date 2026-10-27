from django.shortcuts import get_object_or_404, render
from .models import Post

def index(request):
    posts = Post.objects.order_by('-date_created')
    total_posts = posts.count()
    context = {
        'posts': posts,
        'total_posts': total_posts
    }
    return render(request, 'blog/index.html', context)

def post_filter(request,name):
    posts = Post.objects.filter(author=name)
    total_posts = Post.objects.count()
    context = {
        'posts': posts,
        'total_posts': total_posts
    }
    return render(request, 'blog/post_filter.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post,
        'total_posts': Post.objects.count()
    }
    return render(request, 'blog/post_detail.html', context)

def latest_posts(request):
    post = Post.objects.last()
    context = {
        'post' : post,
        'total_posts' : Post.objects.count()
    }
    return render(request,'blog/latest_post.html',context)

def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def base(request):
    return render(request, 'blog/base.html')

def contact(request):
    context = {
        "message" : "Feel free to reach out to us!",
        "available" : False,
        "contacts" : [
            {"email": "info@example.com", "phone": "123-456-7890"},
            {"email": "support@example.com", "phone": "098-765-4321"}
        ]
    }
    return render(request, 'blog/contact.html', context)