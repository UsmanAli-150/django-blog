from django.shortcuts import get_object_or_404, render, redirect
from .models import Post
from .forms import PostForm

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

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'blog/create_post.html', context)

def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)   # edit THIS post
        if form.is_valid():
            form.save()                                # UPDATE, not INSERT
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)                 # form pre-filled
    return render(request, 'blog/create_post.html', {'form': form})

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':      # only a real confirmed submit deletes
        post.delete()
        return redirect('index')
    return render(request, 'blog/delete_post.html', {'post': post})