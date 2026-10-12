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