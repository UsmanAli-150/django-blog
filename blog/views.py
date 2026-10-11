from django.shortcuts import render

def index(request):
    context = {
        'name': 'Salaar',
        'Semester': '05',
        'Hobbies': ['Coding', 'Gaming', 'Reading']
    }
    return render(request, 'blog/index.html', context)

def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def base(request):
    return render(request, 'blog/base.html')